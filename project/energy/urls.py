from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
     url(r'^admin/', include(admin.site.urls)),
     (r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/index/img/favicon.ico'}),
)

urlpatterns.append(
    url(r'^(.*?)$', 'redokes.views.route')
)