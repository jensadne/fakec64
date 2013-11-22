from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.base import TemplateView


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'fakec64.views.validate_command', name='validate'),
    url(r'^test/$', TemplateView.as_view(template_name='fakec64/test.html'), name='c64test'),

    url(r'^admin/', include(admin.site.urls)),
)
