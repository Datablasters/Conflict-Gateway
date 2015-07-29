from django.conf.urls import patterns, include, url
from django.contrib import admin

handler404 = 'articles.views.custom_404'
admin.site.site_header = 'Conflict Gateway Administration'

urlpatterns = patterns('',
    url(r'^', include('articles.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^tinymce/', include('tinymce.urls')),
)
