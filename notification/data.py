# -*- coding: utf-8 -*-
    

import json
import logging
import md5
import copy
import xlrd
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.core.cache import get_cache
from django.db import transaction
from userprofile.models import (
        AuthUserprofile,
        AuthUser
    )
from notification.models import Notification,NotificationMsg,NotifyMsg
from operation.dict_key import DICT_MAP

cache = get_cache('default')

def pack_notify(request):
    '''封装帖子信息数据
    '''
    page = int(request.GET.get('page',1))
    psize = int(request.GET.get('psize', 20))
    # 收信人ID
    user_id = request.GET.get('user_id', '') 
    # 发送时间开始
    create_time_start = request.GET.get('create_time_start', '') 
    # 发送时间结束
    create_time_end = request.GET.get('create_time_end', '') 
    # 发信人用户名
    update_user = request.GET.get('update_user', '') 
    # 关键字
    keywords = request.GET.get('keywords', '')
    q = NotificationMsg.objects.all()
    q = q.order_by('-create_time')
    # 收信人
    if user_id:
        nfc = Notification.objects.filter(user_id=user_id)
        nfc_ids = [n.id for n in nfc]
        nfm = NotifyMsg.objects.filter(nid__in=nfc_ids)
        nfm_dict = {nf.mid: '' for nf in nfm}
        q = q.filter(id__in=nfm_dict.keys()).order_by('-create_time')
    if create_time_start:
        q = q.filter(create_time__gte=create_time_start)
    if create_time_end:
        create_time_end = create_time_end + " 23:59:59"
        q = q.filter(create_time__lte=create_time_end)
    if update_user:
        q = q.filter(update_user__contains=update_user)
    if keywords:
        q = q.filter(title__contains=keywords)
    total = q.count()                                                                                                                        
    p = Paginator(q, psize)
    notify_list = p.page(page)
    common_json = copy.deepcopy(DICT_MAP['COMMON_LIST_JSON'])
    content_list = []
    for r in notify_list:
        nm_list = NotifyMsg.objects.filter(mid=r.id)
        notify_ids = [nm.nid for nm in nm_list]
        no_ids = Notification.objects.filter(id__in=notify_ids)
        user_ids = [str(no.user_id) for no in no_ids]
        user_ids = ';'.join(user_ids)
        r_json = {
            'id': r.id,
            'create_time': r.create_time.strftime('%Y-%m-%d %H:%M:%S'),
            'title': r.title,
            'user_ids': user_ids,
            'update_user': r.update_user
        }
        content_list.append(r_json)
    common_json['list'] = content_list
    common_json['pages']['page'] = page
    common_json['pages']['recordsPerPage'] = psize
    common_json['pages']['totalRecord'] = total
    common_json['pages']['totalPage'] = (total - 1) / psize + 1
    common_json['statusCode'] = 1
    return common_json

def get_notify(request):
    '''查看单个站内信详情
    '''
    nid = request.GET.get('nid', '')
    nm = NotificationMsg.objects.filter(id=nid)
    notify_json = {'statusCode':1}
    if nm:
        nm = nm[0]
        nm_list = NotifyMsg.objects.filter(mid=nm.id)
        notify_ids = [nmsg.nid for nmsg in nm_list]
        no_ids = Notification.objects.filter(id__in=notify_ids)
        user_ids = [str(no.user_id) for no in no_ids]
        notify_json['user_ids'] = user_ids
        notify_json['update_user'] = nm.update_user
        notify_json['create_time'] = nm.create_time.strftime('%Y-%m-%d %H:%M:%S')
        notify_json['title'] = nm.title
        notify_json['content'] = nm.content
        notify_json['outlink'] = nm.outlink
        notify_json['link_remark'] = nm.link_remark
    return notify_json


@transaction.commit_on_success(using='cms')
def add_notify(request):
    '''添加站内信
    '''
    # 收信人
    user_ids = request.POST.get('user_ids', '')
    title = request.POST.get('title', '')
    content = request.POST.get('content', '')
    link_remark = request.POST.get('link_remark', '')
    outlink = request.POST.get('outlink', '')
    u_res = _check_user_enabled(user_ids) 
    if u_res['statusCode'] <= 0:
        return u_res
    # 保存系统站内信
    # 添加人 
    update_user = ''
    if 'session_id' in request.COOKIES:
        session_id = request.COOKIES['session_id']
        update_user = cache.get(session_id)['username']
    nom = NotificationMsg()
    nom.content = content
    nom.title = title
    nom.outlink = outlink
    nom.link_remark = link_remark
    nom.update_user = update_user
    nom.save()
    # 保存平台站内信
    for uid in user_ids.split(';'):
        outlink = u"""<a href="{}" target="_blank">{}</a>""".format(outlink, link_remark)
        meta = {'content':content, 'outlink': outlink, 'title':title}
        noti = Notification()
        noti.user_id = uid
        noti.type = 'system'
        noti.status = 1
        noti.meta = json.dumps(meta)
        noti.save()
        # 保存站内信对应关系
        nm = NotifyMsg()
        nm.nid = noti.id
        nm.mid = nom.id
        nm.save()
    return {'statusCode':1}

def _check_user_enabled(user_ids):
    try:
        user_arr = user_ids.split(';')
        uid_list = []
        for uid in user_arr:
            uid = uid.strip()
            uid_list.append(uid)
         
        user_list = AuthUser.objects.filter(id__in=uid_list)
        ex_user_id_list = [str(u.id) for u in user_list]
        not_ex_user = set(uid_list) - set(ex_user_id_list)
        if not_ex_user:
            not_ex_str = ','.join(not_ex_user)
            return {'statusCode':0, 'msg': '收件人ID为{}的用户不存在'.format(not_ex_str)}
    except Exception, e:
        return {'statusCode':0, 'msg': '收信人ID输入有误，请检查后重新输入'}
    return {'statusCode':1}


def get_send_users(request):
    '''从excel加载发送用户
    '''
    excel_file = request.FILES['files']
    excel_content = excel_file.file.getvalue()
    data = xlrd.open_workbook(file_contents=excel_content)
    table = data.sheets()[0]
    res = table.col_values(0)
    user_ids = []
    if res:
        user_ids = [int(r) for r in res]
    return {'statusCode':1, 'user_ids':user_ids}



    
