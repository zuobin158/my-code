from django.conf.urls import patterns, url
from django.conf import settings

urlpatterns = patterns(
    '',
    url(r'^list$', 'bbs.views.list'),
    url(r'^update_status$', 'bbs.views.update_status'),
    url(r'^update_tag$', 'bbs.views.update_tag'),
    url(r'^edit_tag$', 'bbs.views.edit_tag'),
    url(r'^save_tags$', 'bbs.views.save_tags'),
)
