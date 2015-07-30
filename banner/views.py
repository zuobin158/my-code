# -*- coding: utf-8 -*-


import json
import logging
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.paginator import Paginator
from operation.dict_key import DICT_MAP
from banner.services import BannerService
from banner.models import Banner


log = logging.getLogger(__name__)

def list(request):
    '''显示banner图列表
    '''
    try:
        res = BannerService().pack_banner(request)
    except Exception,e:
        log.error('method list error, error is %s' % e, exc_info=True)
        res = DICT_MAP['COMMON_LIST_JSON'] 
        res['statusCode'] = -1
    return HttpResponse(json.dumps(res))

def edit(request):
    '''进入编辑界面
    '''
    try:
        res = BannerService().get_banner(request)
    except Exception,e:
        log.error('method edit error, error is %s' % e, exc_info=True)
        res = {'statusCode': -1}
    return HttpResponse(json.dumps(res))

def save(request):
    '''添加或者更新banner
    '''
    try:
        res = BannerService().save_or_update(request)
    except Exception,e:
        log.error('method save error, error is %s' % e, exc_info=True)
        res = {'statusCode': -1}
    return HttpResponse(json.dumps(res))

def hide(request):
    '''隐藏banner
    '''
    res = {'statusCode': 1}
    try:
        banner_id = request.GET.get('banner_id', '')
        is_active = request.GET.get('is_active', '')
        ban = Banner.objects.filter(id=banner_id)
        if ban:
            ban[0].is_active = is_active
            ban[0].save()
            return HttpResponse(json.dumps(res))
    except Exception,e:
        log.error('method hide error, error is %s' % e, exc_info=True)
        res = {'statusCode': -1}
    return HttpResponse(json.dumps(res))
    
def save_order(request):
    try:
        res = {'statusCode':0}
        orderArr = request.POST.get('orderArr', '')
        order_arr = json.loads(orderArr)
        for oa in order_arr:
            ban = Banner.objects.filter(id=oa['bannerId'])
            if ban:
                ban = ban[0]
                ban.order = int(oa['bannerOrder'])
                ban.save()
                res['statusCode'] = 1
    except Exception,e:
        log.error('method save order error, error is %s' % e, exc_info=True)
        res = {'statusCode': -1}
    return HttpResponse(json.dumps(res))

def add_pic(request):
    return render_to_response('upload.html')
    
def upload(request):
    '''上传图片
    '''
    try:
        res = BannerService().upload(request)
    except Exception,e:
        log.error('method upload error, error is %s' % e, exc_info=True)
        res = {'statusCode': -1, 'msg': str(e)}
    return HttpResponse(json.dumps(res))


def publish(request):
    '''发布banner
    '''
    try:
        res = BannerService().publish_banner()
    except Exception,e:
        log.error('method publish error, error is %s' % e, exc_info=True)
        res = {'statusCode': -1, 'msg': str(e)}
    return HttpResponse(json.dumps(res))

def preview_list(request):
    '''获取预览的数据
    '''
    try:
        res = BannerService().get_preview_list()
    except Exception,e:
        log.error('method preview_list error, error is %s' % e, exc_info=True)
        res = {'statusCode': -1, 'msg': str(e)}
    return HttpResponse(json.dumps(res))

def init_banner_data(request):
    '''初始化数据，该功能上线后执行一次
    '''
    try:
        res = BannerService().init_banner_data()
    except Exception,e:
        log.error('method init_banner_data error, error is %s' % e, exc_info=True)
        res = {'statusCode': -1, 'msg': str(e)}
    return HttpResponse(json.dumps(res))

