# Djello
A pretty and configurable admin panel to enhance the default Django Admin Panel based on [Ela Admin](https://github.com/puikinsh/ElaAdmin)

## Version

1.0

## Features

* Converts the default Django Admin panel into a full fledged dashboard into a clean and professional looking Ela Admin
* Sidebar menu with configurable icons
* Top menu with configurable buttons
* New look for all Django Admin pages
* Branding by adding logos
* [Chart js](https://www.chartjs.org/) based widgets which loads data after page load and completely configurable via http apis


## Dependencies

* Django>=2.0
* django-widget-tweaks>=1.4.3

## Installation

Using pip

```
pip install djello
```

## Setup

* Add in app list before 'django.contrib.admin'

```
'djello',
'django.contrib.admin'
...
```

* Add Djello settings in settings.py to configure basic features and dashboard

```
DJELLO = {
    'header_logo': 'djello/images/logo.png',
    'welcome_logo': 'djello/images/logo.png',
    'icons': [],
    'header_links': [('/api/', 'fa-rss'), ('/flower/', 'fa-tasks')],
    'menu': {
        'appauth': {
            'icon': 'fa-users',
            'model_icons': {
                'AppUser': 'fa-user',
                'Role': 'fa-briefcase'}},
        'sample_app': {
            'icon': 'fa-tasks',
            'model_icons': {
                'Post': 'fa-bullhorn'}}},
    'dashboard': [
        [
            {
                'widget': 'stat-widget',
                'id': 'revenue',
                'icon': 'fa-money',
                'color': 'flat-color-1',
                'size': '3',
                'data_url': 'sample_app_api:revenue'
            }, {
                'widget': 'stat-widget',
                'id': 'sales',
                'icon': 'fa-gift',
                'color': 'flat-color-2',
                'size': '3',
                'data_url': 'sample_app_api:sales'
            }, {
                'widget': 'stat-widget',
                'id': 'logsProcessed',
                'icon': 'fa-gears',
                'color': 'flat-color-3',
                'size': '3',
                'data_url': 'sample_app_api:logs_processed'
            }, {
                'widget': 'stat-widget',
                'id': 'peanutsEaten',
                'icon': 'fa-lemon-o',
                'color': 'flat-color-4',
                'size': '3',
                'data_url': 'sample_app_api:peanuts_eaten'
            }
        ],
        [
            {
                'widget': 'graph-widget',
                'id': '',
                'size': '12',
                'data_url': '',
            }
        ],
        [
            {'widget': 'recent-actions-widget', 'id': '', 'size': '6'},
            {'widget': 'chat-widget', 'id': '', 'size': '6'}
        ],
        [
            {
                'widget': 'chartjs-widget',
                'id': 'salesChart',
                'size': '6',
                'data_url': 'sample_app_api:yearly_sales',
            }, {
                'widget': 'chartjs-widget',
                'id': 'barChart',
                'size': '6',
                'data_url': 'sample_app_api:bar_chart',
            }
        ],
        [
            {
                'widget': 'chartjs-widget',
                'id': 'radarChart',
                'size': '6',
                'data_url': 'sample_app_api:radar_chart',
            }, {
                'widget': 'chartjs-widget',
                'id': 'doughnutChart',
                'size': '6',
                'data_url': 'sample_app_api:doughnut_chart',
            }
        ]
    ],
}

```


## Usage


## Future
