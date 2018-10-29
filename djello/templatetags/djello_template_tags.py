from django.contrib.admin import site
from django.apps import apps
from django.utils.text import capfirst
from django.utils import six
from django import template
from django.urls import reverse, NoReverseMatch
from django.utils.html import format_html
from django.contrib.admin.views.main import (
    PAGE_VAR,
)

from django.conf import settings

register = template.Library()


DOT = '.'


@register.simple_tag
def djello_setting(key):
    return settings.DJELLO[key]


@register.inclusion_tag(
    'djello/side_menu.html',
    takes_context=True)
def render_menu_app_list(context):
    # Code adapted from django.contrib.admin.AdminSite
    app_dict = {}
    user = context.get('user')
    for model, model_admin in site._registry.items():
        app_label = model._meta.app_label
        has_module_perms = user.has_module_perms(app_label)

        if has_module_perms:
            perms = model_admin.get_model_perms(context.get('request'))

            # Check whether user has any perm for this module.
            # If so, add the module to the model_list.
            if True in perms.values():
                info = (app_label, model._meta.model_name)
                model_dict = {
                    'name': capfirst(model._meta.verbose_name_plural),
                    'object_name': model._meta.object_name,
                    'perms': perms,
                }
                if perms.get('change', False):
                    try:
                        model_dict['admin_url'] = reverse(
                            'admin:%s_%s_changelist' % info,
                            current_app=site.name
                        )
                    except NoReverseMatch:
                        pass
                if perms.get('add', False):
                    try:
                        model_dict['add_url'] = reverse(
                            'admin:%s_%s_add' % info,
                            current_app=site.name
                        )
                    except NoReverseMatch:
                        pass
                if app_label in app_dict:
                    app_dict[app_label]['models'].append(model_dict)
                else:
                    app_dict[app_label] = {
                        'name': apps.get_app_config(app_label).verbose_name,
                        'app_label': app_label,
                        'app_url': reverse(
                            'admin:app_list',
                            kwargs={'app_label': app_label},
                            current_app=site.name
                        ),
                        'has_module_perms': has_module_perms,
                        'models': [model_dict],
                    }

    # Sort the apps alphabetically.
    app_list = list(six.itervalues(app_dict))
    app_list.sort(key=lambda x: x['name'].lower())

    # Sort the models alphabetically within each sapp.
    for app in app_list:
        app['models'].sort(key=lambda x: x['name'])
        # Adding menu icons from settings
        try:
            app['icon'] = settings.DJELLO['menu'][app['app_label']]['icon']
        except KeyError:
            app['icon'] = None
        for model in app['models']:
            try:
                model['icon'] = settings.DJELLO['menu'][app['app_label']]['model_icons'][model['object_name']]
            except KeyError:
                model['icon'] = None

    return {'app_list': app_list, 'current_url': context.get('request').path}


@register.inclusion_tag(
    'djello/app_model_list.html',
    takes_context=True)
def render_app_model_list(context):
    model_list = []
    user = context.get('user')
    current_url = context.get('request').path

    for model, model_admin in site._registry.items():
        app_label = model._meta.app_label
        has_module_perms = user.has_module_perms(app_label)

        if has_module_perms:
            perms = model_admin.get_model_perms(context.get('request'))

            # Check whether user has any perm for this module.
            # If so, add the module to the model_list.
            if True in perms.values():
                app_url = reverse(
                    'admin:app_list',
                    kwargs={'app_label': app_label},
                    current_app=site.name)

                if current_url == app_url:
                    info = (app_label, model._meta.model_name)
                    model_dict = {
                        'name': capfirst(model._meta.verbose_name_plural),
                        'object_name': model._meta.object_name,
                        'perms': perms,
                    }
                    if perms.get('change', False):
                        try:
                            model_dict['admin_url'] = reverse(
                                'admin:%s_%s_changelist' % info,
                                current_app=site.name)
                        except NoReverseMatch:
                            pass
                    if perms.get('add', False):
                        try:
                            model_dict['add_url'] = reverse(
                                'admin:%s_%s_add' % info,
                                current_app=site.name)
                        except NoReverseMatch:
                            pass

                    try:
                        model_dict['icon'] = settings.DJELLO[
                            'menu'][app_label]['model_icons'][model._meta.object_name]
                    except KeyError:
                        model_dict['icon'] = None

                    model_list.append(model_dict)

    return {'model_list': model_list}


@register.inclusion_tag(
    'djello/dashboard.html',
    takes_context=True)
def render_dashboard(context):
    dashboard_layout = settings.DJELLO['dashboard']
    return {'layout': dashboard_layout, 'user': context.get('user')}


@register.simple_tag
def djello_paginator_number(cl, i):
    """
    Generate an individual page index link in a paginated list.
    """
    if i == DOT:
        return '… '
    elif i == cl.page_num:
        return format_html('<li class="page-item active"><a class="page-link" href="">{}</a></li>', i + 1)
    else:
        return format_html(
            '<li class="page-item"><a class="page-link" href="{}">{}</a></li>',
            cl.get_query_string({PAGE_VAR: i}),
            i + 1)
