# -*- coding: utf-8 -*-
    

import json
import logging
import md5
import copy
from django.http import HttpResponse, HttpResponseRedirect
from django.core.cache import get_cache
from django.core.paginator import Paginator
from django.db.models import Min,Max,Sum
from django.db import transaction
from userprofile.models import (
        UserForbid,
        AuthUserprofile,
        AuthUser
    )
from report.models import BbsReport
from bbs.models import BbsPost, BbsComment, BbsTag, BbsPostTag
from operation.dict_key import DICT_MAP


def pack_post(request):
    '''封装帖子信息数据
    '''
    page = int(request.GET.get('page',1))
    psize = int(request.GET.get('psize', 10))
    # 发帖人昵称
    author_nickname = request.GET.get('author_nickname', '') 
    # 帖子ID
    post_id = request.GET.get('post_id', '') 
    # 发帖时间开始
    create_time_start = request.GET.get('create_time_start', '') 
    # 发帖时间结束
    create_time_end = request.GET.get('create_time_end', '') 
    # 是否隐藏
    status = request.GET.get('status', '') 
    # 关键字
    keywords = request.GET.get('keywords', '')
    q = BbsPost.objects.all()
    if post_id:
        q = q.filter(id=post_id)
    if author_nickname:
        users = AuthUserprofile.objects.filter(nickname__contains=author_nickname)    
        uids = []
        if users:
            uids = [u.user_id for u in users]
        q = q.filter(user_id__in=uids)
    if create_time_start:
        q = q.filter(created_time__gte=create_time_start)
    if create_time_end:
        create_time_end += ' 23:59:59'
        q = q.filter(created_time__lte=create_time_end)
    if status:
        if status == '1':
            q = q.filter(status=-1)
        if status == '0':
            q = q.filter(status__gte=0)
    if keywords:
        q = q.filter(title__contains=keywords)
    q = q.order_by('-created_time')
    total = q.count()                                                                                                                        
    p = Paginator(q, psize)
    post_list = p.page(page)

    common_json = copy.deepcopy(DICT_MAP['COMMON_LIST_JSON'])
    content_list = []
    tag_list = BbsTag.objects.all()
    tag_json = []
    if tag_list:
        for tag in tag_list:
            t = {
                'id': tag.id,
                'name': tag.name,
                'isChecked': 0
            }
            tag_json.append(t)
    for r in post_list:
        aup = AuthUserprofile.objects.filter(user_id=r.user_id)
        bpt_list = BbsPostTag.objects.filter(post_id=r.id)
        tag_res_json = copy.deepcopy(tag_json)
        if bpt_list:
            tag_dict = {t.tag.id: '' for t in bpt_list}
            if tag_res_json:
                for tj in tag_res_json:
                   if tj['id'] in tag_dict:
                       tj['isChecked'] = 1
        r_json = {
            'id': r.id,
            'author_nickname': aup[0].nickname if aup else '', 
            'title': r.title,
            'createDate': r.created_time.strftime('%Y-%m-%d'),
            'status': r.status,
            'tags': tag_res_json 
        }
        content_list.append(r_json)
    common_json['list'] = content_list
    common_json['pages']['page'] = page
    common_json['pages']['recordsPerPage'] = psize
    common_json['pages']['totalRecord'] = total
    common_json['pages']['totalPage'] = (total - 1) / psize + 1
    return common_json

def update_post_status(request):
    '''修改帖子隐藏状态
    '''
    post_id = request.GET.get('post_id', '')
    status = request.GET.get('hideAction', '')
    bp = BbsPost.objects.filter(id=post_id)
    if bp:
        bp[0].status = -1 if status == 'true' else 0
        bp[0].save()
        return {'statusCode': 1}
    return {'statusCode': 0}

def update_post_tag(request):
    '''修改标签
    '''
    post_id = request.GET.get('post_id', '')
    tags = request.GET.get('tags', '')
    bpt = BbsPostTag.objects.filter(post_id=post_id)
    if bpt:
        bpt.delete()
    if tags:
        tag_list = tags.split(',')
        for t in tag_list:
            if t:
                bt = BbsPostTag()
                bt.post_id = post_id
                bt.tag_id = t
                bt.save()
    return {'statusCode': 1}

def get_tags(request):
    '''获取所有标签信息
    '''
    tag_list = BbsTag.objects.all()
    common_json = copy.deepcopy(DICT_MAP['COMMON_LIST_JSON'])
    res_list = []
    for tag in tag_list:
        tag_json = {
            'tagId': tag.id,
            'label': tag.name
        }
        res_list.append(tag_json)
    max_id = tag_list.aggregate(Max('id'))['id__max']
    while len(res_list)<10:
        max_id += 1
        res_list.append({'tagId':max_id, 'label':''})
    common_json['statusCode'] = 1
    common_json['list'] = res_list
    return common_json

@transaction.commit_on_success(using='cms')
def save_all_tags(request):
    '''保存所有的标签信息
    '''
    tags = request.POST.get('tags', '')
    tag_list = json.loads(tags)
    need_delete_ids = []
    for tag in tag_list:
        if tag['label']:
            bt = BbsTag.objects.filter(id=tag['tagId'])
            if bt:
                bt[0].name = tag['label']
                bt[0].save()
            else:
                max_tag_dict = BbsTag.objects.all().aggregate(Max('slug'))
                nbt = BbsTag()
                nbt.name = tag['label']
                nbt.slug = int(max_tag_dict['slug__max']) + 1
                nbt.save()
        else:
            need_delete_ids.append(tag['tagId'])
    del_tag_list = BbsTag.objects.filter(id__in=need_delete_ids)
    del_tag_list.delete()
    return {'statusCode':1}

    

