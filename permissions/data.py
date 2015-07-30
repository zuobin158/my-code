# -*- coding: utf-8 -*-
    
import logging
import md5
from django.http import HttpResponse, HttpResponseRedirect
from django.core.cache import get_cache
from util.json_request import JsonResponse
from ldap import LDAPService
from permissions.models import (
        User,
        System,
        Resources,
        Group,
        Menu
    )
from operation.dict_key import DICT_MAP


cache = get_cache('default')

def save_user_info(session_id, u):
    '''把用户信息缓存到memcache
    Args:
        session_id: 用户唯一标示
        u: 用户信息
    '''
    # 获取该用户的系统资源集合
    sys_res_dict = _get_user_permissions(u)
    # 获取用户的菜单
    menu_list = _pack_user_menu(sys_res_dict) 
    auth_list = _pack_user_permissions(sys_res_dict)
    user_info = {
        'id': u.id,
        'username': u.name,
        'is_active': u.is_active,
        'auth': auth_list,
        'menu': menu_list
    }
    cache.set(session_id, user_info, timeout=DICT_MAP['SESSION_EXPIRE_TIME'])

def check_user_expire(session_id):
    '''检查用户是否过期
    Args:
        session_id: 用户session
    '''
    if cache.get(session_id):
        return True
    return False

def user_logout(session_id):
    '''注销操作
    '''
    if session_id:
        cache.delete(session_id)

def _pack_user_menu(sys_res):
    '''封装用户的菜单
    Args:
        sys_res: 系统对应的资源集合
        eg: {system_id: res_list}
    '''
    menu_dict = {}
    for sys_id in sys_res.keys():
        sys_res_list = sys_res[sys_id]
        # 资源id集合 
        res_ids = [s.id for s in sys_res_list]
        if res_ids:
            # 父节点菜单
            sys_menu_list = Menu.objects.\
                filter(resource_id__in=res_ids,parent_id__isnull=True).order_by('order')
            for parent_menu in sys_menu_list:
                # 二级菜单
                child_menu_list = Menu.objects.\
                    filter(parent_id=parent_menu.id,\
                        resource_id__in=res_ids).order_by('order')
                for child_menu in child_menu_list:
                    # 叶子节点菜单
                    leaf_menu_list = Menu.objects.filter(parent_id=child_menu.id,\
                            resource_id__in=res_ids).order_by('order')
                    # 添加叶子节点   
                    child_menu.child = leaf_menu_list
                # 添加子节点
                parent_menu.child = child_menu_list
        menu_dict[sys_id] = menu_tree(sys_menu_list)
    return menu_dict
                    
def menu_tree(sys_menu_list):
    '''递归对菜单及其子菜单进行封装
    Args:
        sys_menu_list: 子系统的菜单集合
    Returns:
        层级树状菜单json
    '''
    if sys_menu_list and hasattr(sys_menu_list[0], 'child'):
        cm_list = []
        # 如果有child，继续递归封装
        for sml in sys_menu_list:
            content = _pack_common_json(sml)
            if hasattr(sml, 'child'):
                content['child'] = menu_tree(sml.child)
            cm_list.append(content)
        return cm_list

    # 如果是叶子节点，则直接封装返回
    leaf_list = []
    for ll in sys_menu_list:
        leaf_dict = _pack_common_json(ll)
        leaf_list.append(leaf_dict)
    return  leaf_list

def _pack_common_json(obj):
    common_dict = {
        'id' : obj.id,
        'name' : obj.name,
        'mkey' : obj.mkey,
        'resource_id' : obj.resource_id,
        'order' : obj.order,
        'url' : obj.url
    }
    return common_dict

def _get_user_permissions(u):
    '''获取该用户的所有资源
    Args:
        u: 用户
    Returns:
        sys_res: 系统对应的资源集合
    '''
    # 获取该用户所有的角色
    SUPER = '1'
    groups = u.groups.all()
    resource_list = []
    # 获得该用户的所有权限
    if u.is_super == SUPER:
        resource_list = Resources.objects.all() 
    else:
        if groups:
            for g in groups:
                resources = g.resources.all()
                resource_list += resources
    res = {}
    if not resource_list:
        return None
    res = {resou.id : '' for resou in resource_list}
    res = res.keys()
    # 遍历所有子系统
    sys_list = System.objects.all()
    sys_res = {}
    for syst in sys_list:
        # 查询出每个系统的资源
        sys_res_list = Resources.objects.filter(id__in=res,system_id_id=syst.id)
        sys_res[syst.skey] = sys_res_list 
    return sys_res
    
def _pack_user_permissions(sys_res_dict):
    '''封装用户权限
    Args:
        sys_res_dict: 用户系统权限
    Returns:
        user_per_dict: 用户权限，key为权限id
    '''
    user_per_dict = {}
    for key in sys_res_dict.keys():
        # 每个系统的权限集合
        res_content = sys_res_dict[key]
        res_dict = {}
        for res in res_content:
            res_json = {
                'id':res.id,
                'name':res.name,
                'ext_content':res.ext_content
            }
            res_dict[res.id] = res_json
        user_per_dict[key] = res_dict
    return user_per_dict

def login_check():
    '''登录验证修饰器，该修饰器一般应用在
       系统的路由方法中用来验证用户是否登录
       或者用户会话是否过期
    Args:
        request: http请求对象
    '''
    def wrapper(func):
        def login_check_wrapper_func(request, *args, **kwargs):
            if hasattr(request, 'COOKIES') and 'sessionid' in request.COOKIES:
                session_id = request.COOKIES['sessionid']
                if cache.has_key(session_id):
                    return func(request, *args, **kwargs)
            return HttpResponseRedirect('/')
        return login_check_wrapper_func
    return wrapper

def get_user(request):
    '''获取用户信息
    '''
    session_id = request.COOKIES['session_id']
    user_info = cache.get(session_id)
    user_id = user_info.get('id', '')
    user_json = {'statusCode':0}
    if user_id:
        user = User.objects.filter(id=user_id)
        if user:
            user = user[0]
            gs = [g.name for g in user.groups.all()]
            gs = ','.join(gs)
            user_json['statusCode'] = 1
            user_json['real_name'] = user.real_name
            user_json['username'] = user.name
            user_json['email'] = user.email
            user_json['mobile'] = user.phone
            user_json['role'] = gs
    return user_json

def reset_user_pwd(request):
    pwd = request.POST.get('reset_pwd', '')
    session_id = request.COOKIES['session_id']
    user = cache.get(session_id)
    if user:
        user_id = user['id']
        usr = User.objects.filter(id=user_id)
        usr = usr[0]
        md5_pwd = md5.new(pwd).hexdigest()
        usr.pwd = md5_pwd 
        usr.save()
        return {'statusCode':1}
    return {'statusCode':0}


