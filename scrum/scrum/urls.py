from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = patterns('',
    url(r'^api/token/', obtain_auth_token, name='api-token'),
)

