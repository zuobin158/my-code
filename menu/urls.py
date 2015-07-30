from django.conf.urls import patterns, url
from django.conf import settings

urlpatterns = patterns(
    '',
    url(r'^list$', 'menu.views.list'),
    url(r'^get_all_menu$', 'menu.views.get_all_menu'),
    url(r'^save$', 'menu.views.save'),
    url(r'^edit$', 'menu.views.edit'),
    url(r'^delete$', 'menu.views.delete'),
)
