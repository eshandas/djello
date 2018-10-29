from django.conf.urls import url

from .api_views import (
    LoginAPI,
    LogoutAPI,
    TestAPI,
)

urlpatterns = [
    url(r'^login/$', LoginAPI.as_view(), name='login'),
    url(r'^logout/$', LogoutAPI.as_view(), name='logout'),
    url(r'^test/$', TestAPI.as_view(), name='test'),
]
