from django.conf.urls import patterns, url
from django.conf import settings

urlpatterns = patterns(
    '',
    url(r'^list$', 'report.views.list'),
    url(r'^post_detail$', 'report.views.post_detail'),
    url(r'^update_status$', 'report.views.update_status'),
)
