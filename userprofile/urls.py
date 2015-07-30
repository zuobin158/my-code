from django.conf.urls import patterns, url
from django.conf import settings

urlpatterns = patterns(
    '',
    url(r'^list$', 'userprofile.views.list'),
    url(r'^forbid_user$', 'userprofile.views.forbid_user'),
)
