# -*- coding: utf-8 -*-


import json
import logging
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from operation.dict_key import DICT_MAP
from per_resource.services import ResourceService


log = logging.getLogger(__name__)


def get_all_resource(request):
    '''显示全部资源
    '''
    try:
        system_id = request.GET.get('system_id', '')
        res = ResourceService().get_all_resource(system_id)
    except Exception,e:
        log.error('method get_all_resource error, error is %s' % e, exc_info=True)
        res = {'statusCode': -1}
    return HttpResponse(json.dumps(res))

def list(request):
    '''显示资源列表
    '''
    try:
        res = ResourceService().pack_resource(request)
    except Exception,e:
        log.error('method list error, error is %s' % e, exc_info=True)
        res = DICT_MAP['COMMON_LIST_JSON'] 
        res['statusCode'] = -1
    return HttpResponse(json.dumps(res))

def delete(request):
    '''删除资源
    '''
    try:
        resource_id = request.GET.get('id', '')
        res = ResourceService().delete_resource(resource_id)
    except Exception,e:
        log.error('method delete error, error is %s' % e, exc_info=True)
        res = {'statusCode': -1, 'msg':'程序内部异常，请稍后再试！'}
    return HttpResponse(json.dumps(res))

def get_system_list(request):
    '''获取所有子系统
    '''
    try:
        res = ResourceService().get_system_list()
    except Exception,e:
        log.error('method get_system_list error, error is %s' % e, exc_info=True)
        res = {'statusCode': -1}
    return HttpResponse(json.dumps(res))

def edit(request):
    '''编辑资源，获取单个资源信息
    '''
    try:
        resource_id = request.GET.get('id', '')
        res = ResourceService().get_resource(resource_id)
    except Exception,e:
        log.error('method edit error, error is %s' % e, exc_info=True)
        res = {'statusCode': -1}
    return HttpResponse(json.dumps(res))

def save(request):
    '''新增或修改资源:
    '''
    try:
        res = ResourceService().save_or_update(request)
    except Exception,e:
        log.error('method save error, error is %s' % e, exc_info=True)
        res = {'statusCode': -1}
    return HttpResponse(json.dumps(res))



