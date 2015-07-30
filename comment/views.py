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
from comment.data import pack_comment


log = logging.getLogger(__name__)


def list(request):
    '''显示评论列表
    '''
    try:
        res = pack_comment(request)
    except Exception,e:
        log.error('method list error, error is %s' % e, exc_info=True)
        res = DICT_MAP['COMMON_LIST_JSON'] 
        res['statusCode'] = -1
    return HttpResponse(json.dumps(res))

def delete(request):
    '''删除评论，假删除
    '''
    res = {'statusCode': 0}
    try:
        comment_id = request.GET.get('comment_id', '')
        bc = BbsComment.objects.filter(id=comment_id)
        if bc:
            bc[0].status = -1
            bc[0].save()
            res['statusCode'] = 1
    except Exception,e:
        log.error('method list error, error is %s' % e, exc_info=True)
        res['statusCode'] = -1
    return HttpResponse(json.dumps(res))

