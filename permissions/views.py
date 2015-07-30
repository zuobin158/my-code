# -*- coding: utf-8 -*-
    
import logging
import md5
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.shortcuts import render_to_response
from util.json_request import JsonResponse
from ldap import LDAPService
from permissions.models import User
from permissions.data import (
        save_user_info,
        user_logout,
        login_check,
        get_user,
        reset_user_pwd
    )
from operation.dict_key import DICT_MAP

log = logging.getLogger(__name__)

def main(request):
    return render_to_response('main.html')

def index(request):
    '''登录界面
    '''
    return render_to_response('login.html')

def reset(request):
    '''重置密码
    '''
    return render_to_response('reset.html')

def login(request):
    '''验证登录
    '''
    # 验证是否是post请求
    if request.method == 'POST':
        if 'name' not in request.POST or 'password' not in request.POST:
            js = {
                'statusCode': 0
            }
            return JsonResponse(js)
        name = request.POST['name']
        password = request.POST['password']
        # 验证用户名密码是否正确
        try:
            u = _check_login(name, password)
            if u:
                return login_success(request, u)
        except Exception as e:
            log.error('Error is %s' % e, exc_info=True)
            raise
        js = {
            'statusCode': 0
        }
        return JsonResponse(js)

def login_success(request, u):
    '''登录成功后进行跳转子系统
    Args:
        request: 请求
        name: 用户名
    '''
    res = {'statusCode': 0}
    try:
        # 保存sessionid和用户信息到memcached
        session_id = request.COOKIES['session_id']
        save_user_info(session_id, u)
        res['statusCode'] = 1
    except Exception, e:
        res = {'statusCode':-1}
        log.error('Error is %s'% e, exc_info=True) 
    return JsonResponse(res)

def logout(request):
    '''注销操作
    '''
    try:
        session_id = request.GET.get('session_id')
        if not session_id:
            session_id = request.COOKIES['session_id']
        user_logout(session_id)
        return render_to_response('login.html')
    except Exception, e:
        log.error('Error is %s'% e, exc_info=True) 
    return render_to_response('error.html')

def _check_login(name, pwd):
    '''验证登录
    '''
    md5_pwd = md5.new(pwd).hexdigest()
    u = User.objects.filter(name=name,pwd=md5_pwd,is_active='1')
    if u:
        return u[0]
    return None

def reset_pwd(request):
    '''重置密码
    '''
    try:
        res = reset_user_pwd(request)
    except Exception, e:
        res = {'statusCode':-1}
        log.error('Error is %s'% e, exc_info=True) 
    return JsonResponse(res)

def get_user_info(request):
    try:
        res = get_user(request)
    except Exception, e:
        res = {'statusCode':-1}
        log.error('Error is %s'% e, exc_info=True) 
    return JsonResponse(res)
