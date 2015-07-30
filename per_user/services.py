# -*- coding: utf-8 -*-
    

import json
import logging
import md5
import copy
from django.http import HttpResponse, HttpResponseRedirect
from django.core.cache import get_cache
from django.core.paginator import Paginator
from django.db import transaction
from permissions.models import (
        User,
        System,
        Resources,
        Group,
        Menu
    )
from operation.dict_key import DICT_MAP
from common.decorator import singleton


@singleton
class PerUserService(object):

    def pack_user(self, request):
        '''封装帖子信息数据
        '''
        page = int(request.GET.get('page',1))
        psize = int(request.GET.get('psize', 10))
        # 姓名
        real_name = request.GET.get('real_name', '') 
        # 用户名
        name = request.GET.get('name', '') 
        # 邮箱
        email = request.GET.get('email', '')
        # 手机号
        phone = request.GET.get('phone', '')
        # 角色
        group_id = request.GET.get('group_id', '')
        # 状态
        is_active = request.GET.get('is_active', '')
        q = User.objects.all()
        if real_name:
            q = q.filter(real_name__contains=real_name)
        if name:
            q = q.filter(name__contains=name)
        if email:
            q = q.filter(email__contains=email)
        if phone:
            q = q.filter(phone__contains=phone)
        if group_id:
            q = q.filter(groups__id=group_id)
        if is_active:
            q = q.filter(is_active=is_active)
        total = q.count()
        p = Paginator(q, psize)
        user_list = p.page(page)

        common_json = copy.deepcopy(DICT_MAP['COMMON_LIST_JSON'])
        content_list = []
        for r in user_list:
            user_groups = r.groups.all()
            usergroup = ','.join([ug.name for ug in user_groups])
            ur_list = []
            for usgr in user_groups:
                ur_list += usgr.resources.all()
            authorities = {ul.name: '' for ul in ur_list}
            authorities = ';'.join(authorities.keys())
            r_json = {
                'id': r.id,
                'name': r.name,
                'email': r.email,
                'phone': r.phone,
                'real_name': r.real_name, 
                'usergroup': usergroup,
                'authorities': authorities,
                'is_active': r.is_active,
                'is_super': r.is_super
            }
            content_list.append(r_json)
        common_json['statusCode'] = 1
        common_json['list'] = content_list
        common_json['pages']['page'] = page
        common_json['pages']['recordsPerPage'] = psize
        common_json['pages']['totalRecord'] = total
        common_json['pages']['totalPage'] = (total - 1) / psize + 1
        return common_json

    def get_per_user(self, request):
        user_id = request.GET.get('userId', '')
        u = User.objects.filter(id=user_id)
        user_json = {'statusCode':1, 'user':''}
        if u:
            u = u[0]
            group_list = Group.objects.all()
            user_group_dict = {gr.id:"" for gr in u.groups.all()}
            group_auth_list = []
            for g in group_list:
                res_list =[r.name for r in g.resources.all()]
                authorities = ';'.join(res_list)
                ga_dict = {
                    'id': g.id,#组id
                    'role': g.name,
                    'authorities': authorities,
                    'is_checked': 1 if g.id in user_group_dict else 0
                }
                group_auth_list.append(ga_dict) 
            user_dict = {
                'id': u.id,
                'real_name': u.real_name,
                'name': u.name,
                'email': u.email,    
                'phone': u.phone,
                'is_super': u.is_super,
                'is_active': u.is_active,
                'group_auth_list': group_auth_list

            }            
            user_json['user'] = user_dict
        return user_json
        
    def get_group_auth(self, request):
        '''获取所有的组和对应的资源
        '''
        group_list = Group.objects.all()
        group_json = {'statusCode':1, 'group_auth_list':[]}
        auth_list = []
        for gr in group_list:
            res_list =[r.name for r in gr.resources.all()]
            authorities = ';'.join(res_list)
            group_dict = {
                'id': gr.id,
                'role': gr.name,
                'authorities': authorities
            }
            auth_list.append(group_dict)
        group_json['group_auth_list'] = auth_list
        return group_json


    @transaction.commit_on_success()
    def save_or_update(self, request):
        '''保存或添加用户
        '''
        user_id = request.POST.get('userId', '')
        # 姓名
        real_name = request.POST.get('real_name', '') 
        # 用户名
        name = request.POST.get('name', '') 
        # 邮箱
        email = request.POST.get('email', '')
        # 手机号
        phone = request.POST.get('phone', '')
        # 是否启用
        is_active = request.POST.get('is_active', '')
        # 是否管理员
        is_super = request.POST.get('is_super', '')
        # 角色
        group_ids = request.REQUEST.getlist('groups_ids[]')
        if user_id:
            # 如果用户id存在，则修改
            user = User.objects.get(id=user_id)
            user.groups.clear()
        else:
            # 添加新用户
            user = User()
            user.name = name
            user.pwd = md5.new(DICT_MAP['DEFAULT_PWD']).hexdigest() 
        user.real_name = real_name
        user.is_active = is_active
        user.is_super = is_super
        user.email = email
        user.phone = phone
        user.save()
        new_groups = Group.objects.filter(id__in=group_ids)
        for ng in new_groups:
            user.groups.add(ng)
        return {'statusCode': 1}

