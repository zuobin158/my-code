# -*- coding: utf-8 -*-


import json
import logging
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.paginator import Paginator
from permissions.models import User
from operation.dict_key import DICT_MAP
from per_user.services import PerUserService


log = logging.getLogger(__name__)


def list(request):
    '''显示用户列表
    '''
    try:
        res = PerUserService().pack_user(request)
    except Exception,e:
        log.error('method list error, error is %s' % e, exc_info=True)
        res = DICT_MAP['COMMON_LIST_JSON'] 
        res['statusCode'] = -1
    return HttpResponse(json.dumps(res))

def edit(request):
    '''进入编辑详情页
    '''
    try:
        res = PerUserService().get_per_user(request)
    except Exception,e:
        log.error('method edit error, error is %s' % e, exc_info=True)
        res = {'statusCode': -1}
    return HttpResponse(json.dumps(res))
   
def add(request):
    '''添加新用户
    '''
    try:
        res = PerUserService().get_group_auth(request)
    except Exception,e:
        log.error('method add error, error is %s' % e, exc_info=True)
        res = {'statusCode': -1}
    return HttpResponse(json.dumps(res))

def save(request):
    '''添加或修改用户
    '''
    try:
        res = PerUserService().save_or_update(request)
    except Exception,e:
        log.error('method save error, error is %s' % e, exc_info=True)
        res = {'statusCode': -1}
    return HttpResponse(json.dumps(res))

def delete(request):
    '''删除用户
    '''
    res = {'statusCode':1}
    try:
        user_id = request.GET.get('user_id', '')
        u = User.objects.get(id=user_id)
        u.delete()
    except Exception,e:
        log.error('method delete error, error is %s' % e, exc_info=True)
        res = {'statusCode': -1}
    return HttpResponse(json.dumps(res))



