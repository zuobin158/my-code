from django.conf.urls import patterns, url
from django.conf import settings

urlpatterns = patterns(
    '',
    url(r'^get_group_list$', 'group.views.get_group_list'),
    url(r'^list$', 'group.views.list'),
    url(r'^delete$', 'group.views.delete'),
    url(r'^save$', 'group.views.save'),
)
