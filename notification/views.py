# -*- coding: utf-8 -*-


import json
import logging
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.paginator import Paginator
from userprofile.models import (
        UserForbid,
        AuthUserprofile,
        AuthUser
    )
from operation.dict_key import DICT_MAP
from notification.data import (
        pack_notify, 
        get_notify,
        add_notify,
        get_send_users
    )


log = logging.getLogger(__name__)


def list(request):
    '''显示用户列表
    '''
    try:
        res = pack_notify(request)
    except Exception,e:
        log.error('method list error, error is %s' % e, exc_info=True)
        res = DICT_MAP['COMMON_LIST_JSON'] 
        res['statusCode'] = -1
    return HttpResponse(json.dumps(res))

def show_detail(request): 
    try:
        res = get_notify(request)
    except Exception,e:
        log.error('method show_detail error, error is %s' % e, exc_info=True)
        res['statusCode'] = -1
    return HttpResponse(json.dumps(res))
    
def save_notify(request):
    '''添加站内信
    '''
    try:
        res = add_notify(request)
    except Exception, e:
        log.error('method save_notify error, error is %s' % e, exc_info=True)
        res['statusCode'] = -1
        res['msg'] = '程序内部异常'
    return HttpResponse(json.dumps(res))

def load_send_users(request):
    '''从excel读取发送用户的id
    '''
    try:
        res = get_send_users(request)
    except Exception, e:
        log.error('method load_send_users error, error is %s' % e, exc_info=True)
        res['statusCode'] = -1
    return HttpResponse(json.dumps(res))



