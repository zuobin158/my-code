from django.conf.urls import patterns, url
from django.conf import settings

urlpatterns = patterns(
    '',
    url(r'^list$', 'comment.views.list'),
    url(r'^delete$', 'comment.views.delete'),
)
