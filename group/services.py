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
from per_resource.services import ResourceService


@singleton
class GroupService(object):

    def pack_group(self, request):
        '''封装角色信息数据
        '''
        page = int(request.GET.get('page',1))
        psize = int(request.GET.get('psize', 10))
        name = request.GET.get('name', '') 
        q = Group.objects.all()
        if name:
            q = q.filter(name__contains=name)
        total = q.count()
        p = Paginator(q, psize)
        group_list = p.page(page)

        common_json = copy.deepcopy(DICT_MAP['COMMON_LIST_JSON'])
        content_list = []
        for r in group_list:
            res_names = ';'.join([res.name for res in r.resources])
            r_json = {
                'id': r.id,
                'name': r.name,
                'created': r.created.strftime('%Y-%m-%d'),
                'modified': r.modified.strftime('%Y-%m-%d'),
                'resources_name': res_names
            }
            content_list.append(r_json)
        common_json['statusCode'] = 1
        common_json['list'] = content_list
        common_json['pages']['page'] = page
        common_json['pages']['recordsPerPage'] = psize
        common_json['pages']['totalRecord'] = total
        common_json['pages']['totalPage'] = (total - 1) / psize + 1
        return common_json

    def get_role_list(self, request):
        '''获取角色列表
        '''
        group_list = Group.objects.all()
        group_json = {'statusCode':1, 'list':[]}
        gr_list = []
        for gr in group_list:
            gr_dict = {
                'id': gr.id,
                'name': gr.name
            }
            gr_list.append(gr_dict)
        group_json['list'] = gr_list
        return group_json

    def delete_group(self, group_id):
        '''删除角色
        '''
        u = User.objects.filter(groups__id=group_id)
        if u:
            return {'statusCode':0, 'msg':'该角色已经有人员使用，无法删除'}
        g = Group.objects.get(id=group_id)
        g.delete()
        return {'statusCode':1, 'msg':''}


    @transaction.commit_on_success()
    def save_or_update(self, request):
        '''新增或修改角色
        '''
        group_id = request.POST.get('id', '')
        name = request.POST.get('name', '')
        resource_list = request.POST.get('resource_list', '')
        resource_list = json.loads(resource_list)
        if group_id:
            group = Group.objects.get(id=group_id)
            group.resources.clear()
        else:
            group = Group()
        group.name = name
        if resource_list:
            new_res_list = Resources.objects.filter(id__in=resource_list)
            if new_res_list:
                for nr in new_res_list:
                    group.resources.add(nr)
        group.save()
        return {'statusCode':1}
        
    def get_group_resource(self, group_id):
        '''获取角色的资源信息，编辑界面使用
        '''
        group = Group.objects.get(id=group_id)
        exist_res = {gr.id: '' for gr in group.resources.all()}
        system_list = ResourceService().get_system_list()['list']
        resource_list = []
        for sys in system_list:
            sys_resource = ResourceService().get_all_resource(sys['id'])
            if sys_resource['list']:
                for sr in sys_resource['list']:
                    sr['is_checked'] = 0
                    if sr['id'] in exist_res:
                        sr['is_checked'] = 1
                sys_res_dict = {
                    'system_name': sys['name'],
                    'list': sys_resource['list']
                }
                resource_list.append(sys_res_dict)
        group_json = {
            'statusCode': 1,
            'name': group.name,
            'resource_list': resource_list
        } 
        return group_json

