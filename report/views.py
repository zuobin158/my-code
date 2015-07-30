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
from report.models import BbsReport
from bbs.models import BbsPost, BbsComment
from operation.dict_key import DICT_MAP
from report.data import pack_report, pack_post_detail, update_report_status


log = logging.getLogger(__name__)


def list(request):
    '''显示用户列表
    '''
    try:
        res = pack_report(request)
    except Exception,e:
        log.error('method list error, error is %s' % e, exc_info=True)
        res = DICT_MAP['COMMON_LIST_JSON'] 
        res['statusCode'] = -1
    return HttpResponse(json.dumps(res))

def post_detail(request):
    '''帖子详情
    '''
    try:
        res = pack_post_detail(request)
    except Exception,e:
        log.error('method post_detail error, error is %s' % e, exc_info=True)
        res = DICT_MAP['POST_DETAIL_JSON'] 
        res['statusCode'] = -1
    return HttpResponse(json.dumps(res))
        
def update_status(request):
    '''修改举报信息状态
    '''
    try:
        res = update_report_status(request)
    except Exception,e:
        log.error('method update_status error, error is %s' % e, exc_info=True)
        res['statusCode'] = -1
    return HttpResponse(json.dumps(res))
    

