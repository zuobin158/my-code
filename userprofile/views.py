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
from userprofile.data import pack_user
from operation.dict_key import DICT_MAP

log = logging.getLogger(__name__)

def index(request):
    return render_to_response('index.html')

def list(request):
    '''显示用户列表
    '''
    try:
        page = int(request.GET.get('page',1))
        psize = int(request.GET.get('psize', 10))
        nickname = request.GET.get('nickname', '') 
        nickname = nickname.encode('utf-8')
        q = AuthUserprofile.objects.all()
        if nickname:
            q = q.filter(nickname__contains=nickname)
        total = q.count()        
        p = Paginator(q, psize)
        user_list = p.page(page)
        res = pack_user(user_list, page, psize, total)
    except Exception,e:
        log.error('method list error, error is %s' % e, exc_info=True)
        res = DICT_MAP['COMMON_LIST_JSON'] 
        res['statusCode'] = -1
    return HttpResponse(json.dumps(res))

def forbid_user(request):
    '''用户禁言，解禁
    '''
    try:
        user_id = request.POST.get('user_id', '') 
        status = request.POST.get('user_status', '')
        remark = request.POST.get('remark', '')
        res = DICT_MAP['OP_JSON']
        # 禁言的情况
        ex_uf = UserForbid.objects.filter(user_id=user_id)
        if status == 'Y':
            if ex_uf:
                res['statusCode'] = -1
                res['msg'] = '该人员已经禁言'
            else:
                uf = UserForbid()
                uf.user_id = user_id
                uf.forbid = 1
                uf.remark = remark
                uf.save() 
                res['statusCode'] = 200
        # 解禁的情况
        if status == 'N':
            if ex_uf:
                ex_uf[0].delete()
                res['statusCode'] = 200
            else:
                res['statusCode'] = -1
                res['msg'] = '该用户已经解禁'
    except Exception,e:
        logging.error('method forbid_user error, error is %s' % e, exc_info=True)
        res['statusCode'] = -1 
        res['msg'] = '程序内部异常！'
    return HttpResponse(json.dumps(res))


