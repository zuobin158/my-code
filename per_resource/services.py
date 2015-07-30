# -*- coding: utf-8 -*-
    

import json
import logging
import md5
import copy
from django.http import HttpResponse, HttpResponseRedirect
from django.core.cache import get_cache
from django.core.paginator import Paginator
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
class ResourceService(object):

    def pack_resource(self, request):
        '''封装资源数据
        '''
        page = int(request.GET.get('page',1))
        psize = int(request.GET.get('psize', 10))
        resource_id = request.GET.get('id', '')
        name = request.GET.get('name', '') 
        system_id = request.GET.get('system_id', '')
        q = Resources.objects.all()
        if resource_id:
            q = q.filter(id=resource_id)
        if name:
            q = q.filter(name__contains=name)
        if system_id:
            q = q.filter(system_id_id=system_id)
        total = q.count()
        p = Paginator(q, psize)
        resource_list = p.page(page)

        common_json = copy.deepcopy(DICT_MAP['COMMON_LIST_JSON'])
        content_list = []
        for r in resource_list:
            r_json = {
                'id': r.id,
                'name': r.name,
                'system_name': r.system_id.name,
                'description': r.description,
                'created': r.created.strftime('%Y-%m-%d'),
                'modified': r.modified.strftime('%Y-%m-%d')
            }
            content_list.append(r_json)
        common_json['statusCode'] = 1
        common_json['list'] = content_list
        common_json['pages']['page'] = page
        common_json['pages']['recordsPerPage'] = psize
        common_json['pages']['totalRecord'] = total
        common_json['pages']['totalPage'] = (total - 1) / psize + 1
        return common_json

    def get_all_resource(self, system_id):
        '''获取所有的资源
        '''
        res_list = Resources.objects.filter(system_id_id=system_id).order_by('modified')
        res_json = {'statusCode':1, 'list':[]}
        r_list = []
        for res in res_list:
            r_json = {
                'id': res.id,
                'name': res.name
            }
            r_list.append(r_json)
        res_json['list'] = r_list
        return res_json

    def delete_resource(self, resource_id):
        '''删除资源信息
        '''
        menu = Menu.objects.filter(resource_id=resource_id)
        flag = Group.objects.filter(resources__id=resource_id).exists()
        if menu or flag:
            return {'statusCode':0, 'msg':'菜单或角色中已经使用该资源，无法删除！'}
        res = Resources.objects.get(id=resource_id)
        res.delete()
        return {'statusCode':1, 'msg': ''}

    def get_system_list(self):
        '''获取所有子系统
        '''
        sys_list = System.objects.all()
        system_json = {'statusCode':1, 'list':[]}
        s_list = []
        for sys in sys_list:
            s_json = {
                'id': sys.id,
                'name': sys.name
            }
            s_list.append(s_json)
        system_json['list'] = s_list
        return system_json

    def get_resource(self, resource_id):
        '''获取单个资源信息
        '''
        res = Resources.objects.get(id=resource_id)
        system_list = self.get_system_list()['list']
        for sys in system_list:
            sys['is_checked'] = 0
            if sys['id'] == res.system_id.id:
                sys['is_checked'] = 1

        res_json = {
            'statusCode': 1,
            'name': res.name,
            'system_list': system_list,
            'ext_content': res.ext_content,
            'description': res.description
        }
        return res_json

    def save_or_update(request):
        '''新增或修改资源
        '''
        resource_id = request.POST.get('resource_id', '')
        name = request.POST.get('name', '')
        system_id = request.POST.get('system_id', '')
        ext_content = request.POST.get('ext_content', '')
        description = request.POST.get('description', '')
        if resource_id:
            res = Resources.objects.get(id=resource_id)
        else:
            res = Resources()
        res.name = name
        res.system_id = system_id
        res.ext_content = ext_content
        res.description = description
        res.save()
        return {'statusCode':1}

