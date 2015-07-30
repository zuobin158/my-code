from django.conf.urls import patterns, url
from django.conf import settings

urlpatterns = patterns(
    '',
    url(r'^list$', 'per_resource.views.list'),
    url(r'^edit$', 'per_resource.views.edit'),
    url(r'^delete$', 'per_resource.views.delete'),
    url(r'^save$', 'per_resource.views.save'),
    url(r'^get_all_resource$', 'per_resource.views.get_all_resource'),
    url(r'^get_system_list$', 'per_resource.views.get_system_list'),
)
