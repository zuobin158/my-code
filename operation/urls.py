# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'permissions.views.index'),
    url(r'^login_success$', 'permissions.views.login_success'),
    url(r'^login$', 'permissions.views.login'),
    url(r'^logout', 'permissions.views.logout'),
    url(r'^reset$', 'permissions.views.reset'),
    url(r'^reset_pwd$', 'permissions.views.reset_pwd'),
    url(r'^deco$', 'permissions.views.deco_test'),
    url(r'^api/check_login/$', 'permissions.api.check_login'),
    url(r'^api/get_system_menu', 'permissions.api.get_system_menu'),
    url(r'^api/get_all_menu', 'permissions.api.get_all_menu'),
    url(r'^api/get_system_permission', 'permissions.api.get_system_permissions'),
    # 资源模块 
    url(r'^resource/', include('per_resource.urls')),

    url(r'^main$', 'permissions.views.main'),
    # 个人信息
    url(r'^permissions/get_user_info$', 'permissions.views.get_user_info'),

    # 帖子模块
    url(r'^post/', include('bbs.urls')),
    # 线上用户模块
    url(r'^userprofile/', include('userprofile.urls')),
    # 举报模块
    url(r'^report/', include('report.urls')),
    # 评论模块
    url(r'^comment/', include('comment.urls')),
    # 站内信模块
    url(r'^notification/', include('notification.urls')),
    # banner
    url(r'^banner/', include('banner.urls')),
    # 人员模块
    url(r'^per_user/', include('per_user.urls')),
    # 角色模块
    url(r'^group/', include('group.urls')),
    # 菜单模块
    url(r'^menu/', include('menu.urls')),

)
