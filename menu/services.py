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
from per_resource.services import ResourceService


@singleton
class MenuService(object):

    def pack_menu(self, request):
        '''封装菜单数据
        '''
        page = int(request.GET.get('page',1))
        psize = int(request.GET.get('psize', 10))
        # 菜单名称
        name = request.GET.get('name', '') 
        # 父菜单id
        parent_id = request.GET.get('parent_id', '') 
        # 菜单id
        menu_id = request.GET.get('id', '')
        q = Menu.objects.all()
        if name:
            q = q.filter(name__contains=name)
        if menu_id:
            q = q.filter(id=menu_id)
        if parent_id:
            q = q.filter(parent_id=parent_id)
        total = q.count()
        p = Paginator(q, psize)
        menu_list = p.page(page)

        common_json = copy.deepcopy(DICT_MAP['COMMON_LIST_JSON'])
        content_list = []
        for r in menu_list:
            parent_name = ''
            p_menu = Menu.objects.filter(id=r.parent_id)
            if p_menu:
                p_menu = p_menu[0]
                parent_name = p_menu.name
            r_json = {
                'id': r.id,
                'order': r.order,
                'name': r.name,
                'mkey': r.mkey,
                'resource_name': r.resource.name,
                'url': r.url,
                'parent_name': parent_name,
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

    def get_all_menu(self, system_id):
        '''获取所有子系统下的菜单
        '''

        res_list = Resources.objects.all()
        if system_id:
            res = res.filter(system_id_id=system_id)
        res_ids = [r.id for r in res_list]
        menu_list = Menu.objects.filter(resource_id__in=res_ids).order_by('modified')
        menu_json = {'statusCode':1, 'list':[]}
        mn_list = []
        for mn in menu_list:
            mn_dict = {
                'id': mn.id,
                'name': mn.name
            }
            mn_list.append(mn_dict)
        menu_json['list'] = mn_list
        return menu_json
    
    def save_or_update(self, request):
        '''新增，修改
        '''
        # 菜单名称
        name = request.POST.get('name', '') 
        # 父菜单id
        parent_id = request.POST.get('parent_id', '') 
        # 菜单id
        menu_id = request.POST.get('id', '')
        mkey = request.POST.get('mkey', '')
        url = request.POST.get('url', '')
        resource_id = request.GET.get('resource_id', '')
        order = request.GET.get('order', '')
        if menu_id:
            menu = Menu.objects.get(id=menu_id)
        else:
            menu = Menu()
        menu.name = name
        menu.mkey = mkey
        menu.url = url
        menu.resource_id = resource_id
        menu.parent_id = parent_id
        menu.order = order
        menu.save()
        return {'statusCode':1}

    def get_menu(self, menu_id):
        '''获取单个菜单
        '''
        menu = Menu.objects.get(id=menu_id)
        system_name = menu.resource.system_id.name
        system_id = menu.resource.system_id.id
        res_list = ResourceService().get_all_resource(system_id)
        for res in res_list['list']:
            res['is_checked'] = 0
            if res['id'] == menu.resource.id:
                res['is_checked'] = 1
        menu_list = self.get_all_menu(system_id)
        for ml in menu_list['list']:
            ml['is_checked'] = 0
            if ml['id'] == int(menu_id):
                ml['is_checked'] = 1

        menu_json = {
            'statusCode': 1,
            'menu':{
                'id': menu_id,
                'name': menu.name,
                'mkey': menu.mkey,
                'url': menu.url,
                'system_name': system_name,
                'resource_list': res_list['list'],
                'menu_list': menu_list,
                'order': menu.order
            }
        }
        return menu_json

    def delete_menu(self, menu_id):
        '''删除菜单
        '''
        mn = Menu.objects.filter(parent_id=menu_id)
        if mn:
            return {'statusCode': 0, 'msg':'该菜单含有子菜单，不能删除！'}
        dmn = Menu.objects.get(id=menu_id)
        dmn.delete()
        return {'statusCode':1}










