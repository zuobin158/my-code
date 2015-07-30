# -*- coding: utf-8 -*-


import json
import logging
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from operation.dict_key import DICT_MAP
from group.services import GroupService


log = logging.getLogger(__name__)


def get_group_list(request):
    '''显示角色列表，下拉框使用
    '''
    try:
        res = GroupService().get_role_list(request)
    except Exception,e:
        log.error('method get_role_list error, error is %s' % e, exc_info=True)
        res = {'statusCode': -1, 'list': []}
    return HttpResponse(json.dumps(res))

def list(request):                                                     
    '''显示角色列表,列表展示
    '''
    try:
        res = GroupService().pack_group(request)
    except Exception,e:
        log.error('method list error, error is %s' % e, exc_info=True)
        res = DICT_MAP['COMMON_LIST_JSON']
        res['statusCode'] = -1
    return HttpResponse(json.dumps(res))

def delete(request):
    '''删除角色
    '''
    try:
        group_id = request.GET.get('id', '')
        res = GroupService().delete_group(group_id)
    except Exception,e:
        log.error('method get_role_list error, error is %s' % e, exc_info=True)
        res = {'statusCode': -1, 'msg': str(e)}
    return HttpResponse(json.dumps(res))

def save(request):
    '''新增或修改角色
    '''
    try:
        res = GroupService().save_or_update(request)
    except Exception,e:
        log.error('method save error, error is %s' % e, exc_info=True)
        res = {'statusCode': -1}
    return HttpResponse(json.dumps(res))

def edit(request):
    '''进入编辑角色界面
    '''
    try:
        group_id = request.GET.get('id', '')
        res = GroupService().get_group_resource(group_id)
    except Exception,e:
        log.error('method edit error, error is %s' % e, exc_info=True)
        res = {'statusCode': -1}
    return HttpResponse(json.dumps(res))


