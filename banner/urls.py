from django.conf.urls import patterns, url
from django.conf import settings

urlpatterns = patterns(
    '',
    url(r'^list$', 'banner.views.list'),
    url(r'^save$', 'banner.views.save'),                                
    url(r'^save_order$', 'banner.views.save_order'),                    
    url(r'^edit$', 'banner.views.edit'),                                
    url(r'^hide$', 'banner.views.hide'),
    url(r'^add_pic$', 'banner.views.add_pic'),
    url(r'^upload$', 'banner.views.upload'),
    url(r'^publish$', 'banner.views.publish'),
    url(r'^preview_list$', 'banner.views.preview_list'),
    url(r'^init_banner_data$', 'banner.views.init_banner_data'),
)
