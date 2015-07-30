from django.conf.urls import patterns, url
from django.conf import settings

urlpatterns = patterns(
    '',
    url(r'^list$', 'per_user.views.list'),
    url(r'^edit$', 'per_user.views.edit'),
    url(r'^save$', 'per_user.views.save'),
    url(r'^add$', 'per_user.views.add'),
    url(r'^delete$', 'per_user.views.delete'),
)
