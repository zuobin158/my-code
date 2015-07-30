# -*- coding: utf-8 -*-


import json
import logging
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from operation.dict_key import DICT_MAP
from menu.services import MenuService

log = logging.getLogger(__name__)


def list(request):
    '''显示菜单列表
    '''
    try:
        res = MenuService().pack_menu(request)
    except Exception,e:
        log.error('method list error, error is %s' % e, exc_info=True)
        res = DICT_MAP['COMMON_LIST_JSON'] 
        res['statusCode'] = -1
    return HttpResponse(json.dumps(res))

def get_all_menu(request):
    '''获取所有菜单
    '''
    try:
        system_id = request.GET.get('system_id', '')
        res = MenuService().get_all_menu(system_id)
    except Exception,e:
        log.error('method get_all_menu error, error is %s' % e, exc_info=True)
        res['statusCode'] = -1
    return HttpResponse(json.dumps(res))

def save(request):
    '''添加新菜单
    '''
    try:
        res = MenuService().save_or_update(request)
    except Exception,e:
        log.error('method save error, error is %s' % e, exc_info=True)
        res['statusCode'] = -1
    return HttpResponse(json.dumps(res))

def edit(request):
    '''编辑菜单
    '''
    try:
        menu_id = request.GET.get('id', '')
        res = MenuService().get_menu(menu_id)
    except Exception,e:
        log.error('method edit error, error is %s' % e, exc_info=True)
        res['statusCode'] = -1
    return HttpResponse(json.dumps(res))

def delete(request):
    '''删除菜单
    '''
    try:
        menu_id = request.GET.get('id', '')
        res = MenuService().delete_menu(menu_id)
    except Exception,e:
        log.error('method edit error, error is %s' % e, exc_info=True)
        res['statusCode'] = -1
        res['msg'] = '程序内部异常，请稍后再试！'
    return HttpResponse(json.dumps(res))




