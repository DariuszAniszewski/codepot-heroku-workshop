"""codepot_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^$', 'codepot.views.home', name='home'),
    url(r'^logs$', 'codepot.views.log', name='log'),
    url(r'^timeout$', 'codepot.views.timeout', name='timeout'),
    url(r'^save-file$', 'codepot.views.save_file', name='save-file'),
    url(r'^read-file$', 'codepot.views.read_file', name='read-file'),
    url(r'^python-version$', 'codepot.views.python_version', name='python-version'),
    url(r'^memory/(?P<megs>[0-9]+)/$', 'codepot.views.memory', name='memory'),
]
