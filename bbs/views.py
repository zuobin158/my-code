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
from bbs.models import BbsPost, BbsComment
from operation.dict_key import DICT_MAP
from bbs.data import (
        pack_post, 
        update_post_status, 
        update_post_tag,
        get_tags,
        save_all_tags
    )


log = logging.getLogger(__name__)


def list(request):
    '''显示帖子列表
    '''
    try:
        res = pack_post(request)
    except Exception,e:
        log.error('method list error, error is %s' % e, exc_info=True)
        res = DICT_MAP['COMMON_LIST_JSON'] 
        res['statusCode'] = -1
    return HttpResponse(json.dumps(res))

def update_status(request):
    '''修改帖子状态，隐藏，取消隐藏。
    '''
    try:
        res = update_post_status(request)
    except Exception,e:
        log.error('method update_status error, error is %s' % e, exc_info=True)
        res['statusCode'] = -1
    return HttpResponse(json.dumps(res))

def update_tag(request):
    '''修改帖子的标签内容
    '''
    try:
        res = update_post_tag(request)
    except Exception,e:
        log.error('method update_status error, error is %s' % e, exc_info=True)
        res['statusCode'] = -1
    return HttpResponse(json.dumps(res))

def edit_tag(request):
    '''获取标签列表，编辑标签项
    '''
    try:
        res = get_tags(request)
    except Exception,e:
        log.error('method edit_tag error, error is %s' % e, exc_info=True)
        res['statusCode'] = -1
    return HttpResponse(json.dumps(res))

def save_tags(request):
    '''保存标签信息
    '''
    try:
        res = save_all_tags(request)
    except Exception,e:
        log.error('method save_tags error, error is %s' % e, exc_info=True)
        res['statusCode'] = -1
    return HttpResponse(json.dumps(res))


