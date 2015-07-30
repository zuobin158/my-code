from django.conf.urls import patterns, url
from django.conf import settings

urlpatterns = patterns(
    '',
    url(r'^list$', 'notification.views.list'),
    url(r'^show_detail$', 'notification.views.show_detail'),
    url(r'^save_notify$', 'notification.views.save_notify'),
    url(r'^load_send_users$', 'notification.views.load_send_users'),
)
