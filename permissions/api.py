# -*- coding: utf-8 -*-

'''
Copyright (c) 2015,xuetangx
All rights reserved.

摘    要: api.py 对外提供的相关接口
创 建 者: ZuoBin
创建日期: 2015-06-09
'''
    
import logging
import md5
import json
from django.http import HttpResponse, HttpResponseRedirect
from django.core.cache import get_cache
from util.json_request import JsonResponse

cache = get_cache('default')

log = logging.getLogger(__name__)

def check_login(request):
    '''验证是否登录
    '''
    try:
        #session_id = request.GET.get('session_id')
        session_id = request.COOKIES['session_id']
        if not session_id:
            js = {'is_login':False, 'msg':'your session_id is None'}
        elif session_id and cache.has_key(session_id):
            js = {'is_login':True, 'msg':''}
        else:
            js = {'is_login':False, 'msg':'your session is expired,please relogin!'}
        return JsonResponse(js)
    except Exception, e:
        log.error('Error is %s' % e, exc_info=True)
        js = {'is_login':False, 'msg':'权限系统内部异常！'}
        return JsonResponse(js)

def get_system_menu(request):
    '''获取子系统的菜单
       
    '''
    js = {'statusCode':0, 'navs':'', 'msg':'you have no menus on this system!', 'nickname': '访客'}
    try:
        login_js = check_login(request)
        login_dict = json.loads(login_js.content)
        # 检查是否登录，session_id是否传过来
        if login_dict['is_login']:
            session_id = request.COOKIES['session_id']
            res = cache.get(session_id)
            if res and res['menu']:
                sys_key = request.GET.get('skey', 'cms')
                sys_menu = res['menu'][sys_key][0]['child']
                js = {'statusCode':200, 'navs':sys_menu, 'msg':'', 'nickname': res.get('username','')}
        else:
            js['msg'] = 'please login first!'
        return JsonResponse(js)
    except Exception, e:
        log.error('Error is %s' % e, exc_info=True)
        js['msg'] = '权限系统内部异常！'
        return JsonResponse(js)
        

def get_all_menu(request):
    '''获取子系统的菜单
       
    '''
    js = {'statusCode':0, 'navs':'', 'msg':'you have no menus on this system!', 'nickname': '访客'}
    try:
        login_js = check_login(request)
        login_dict = json.loads(login_js.content)
        # 检查是否登录，session_id是否传过来
        if login_dict['is_login']:
            session_id = request.COOKIES['session_id']
            res = cache.get(session_id)
            if res and res['menu']:
                sys_key = request.GET.get('skey', 'cms')
                sys_menu = res['menu'][sys_key]
                js = {'statusCode':200, 'navs':sys_menu, 'msg':'', 'nickname': res.get('username','')}
        else:
            js['msg'] = 'please login first!'
        return JsonResponse(js)
    except Exception, e:
        log.error('Error is %s' % e, exc_info=True)
        js['msg'] = '权限系统内部异常！'
        return JsonResponse(js)

def get_system_permissions(request):
    '''获取子系统的权限
    '''
    js = {'code':0, 'permission':'', 'msg':'you have no persissions on this system!'}
    try:
        login_js = check_login(request)
        login_dict = json.loads(login_js.content)
        # 检查是否登录，session_id是否传过来
        if login_dict['is_login']:
            session_id = request.COOKIES['session_id']
            res = cache.get(session_id)
            if res and res['auth']:
                sys_key = request.GET.get('skey', 'cms')
                permission_id = int(request.GET.get('permission_id', ''))
                if not permission_id:
                    js['msg'] = 'your must provide a correct permission id!'
                    return JsonResponse(js)
                permission = res['auth'][sys_key][permission_id]
                js = {'code':1, 'auth':permission, 'msg':''}
        else:
            js['msg'] = 'please login first!'
        return JsonResponse(js)
    except Exception, e:
        log.error('Error is %s' % e, exc_info=True)
        js['msg'] = '权限系统内部异常！'
        return JsonResponse(js)
 
