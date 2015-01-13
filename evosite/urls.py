# -*- coding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
admin.autodiscover()

import settings
import views

urlpatterns = patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    (r'^(?P<path>favicon.ico)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    (r'^(?P<path>robots.txt)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    (r'^(?P<path>c2120efb315c.html)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    
    url(r'^admin_tools/', include('admin_tools.urls')),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/jsi18n/', 'django.views.i18n.javascript_catalog'),
    url(r'^settings/', include('livesettings.urls')),
    url(r'^ckeditor/', include('ckeditor.urls')),

    url(r'^$', views.page, {'page_name': 'home'}),
    url(r'^(?P<page_name>[\w-]+)/$', views.page),
)
