# -*- coding: utf-8 -*-
    
import logging
import md5
import copy
from django.http import HttpResponse, HttpResponseRedirect
from django.core.cache import get_cache
from django.core.paginator import Paginator
from userprofile.models import (
        UserForbid,
        AuthUserprofile,
        AuthUser
    )
from report.models import BbsReport
from bbs.models import BbsPost, BbsComment, BbsTag, BbsPostTag
from operation.dict_key import DICT_MAP


def pack_comment(request):
    '''封装帖子信息数据
    '''
    page = int(request.GET.get('page',1))
    psize = int(request.GET.get('psize', 20))
    # 发帖人昵称
    author_nickname = request.GET.get('author_nickname', '') 
    # 帖子ID
    post_id = request.GET.get('post_id', '') 
    # 发帖时间开始
    create_time_start = request.GET.get('create_time_start', '') 
    # 发帖时间结束
    create_time_end = request.GET.get('create_time_end', '') 
    # 评论id
    comment_id = request.GET.get('comment_id', '') 
    # 关键字
    keywords = request.GET.get('keywords', '')
    q = BbsComment.objects.all()
    q = q.filter(status__gte=0)
    if post_id:
        q = q.filter(post_id=post_id)
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
    if comment_id:
        q = q.filter(id=comment_id)
    if keywords:
        q = q.filter(title__contains=keywords)
    q = q.order_by('-created_time')
    total = q.count()                                                                                                                        
    p = Paginator(q, psize)
    comment_list = p.page(page)

    common_json = DICT_MAP['COMMON_LIST_JSON']
    content_list = []
    tag_list = BbsTag.objects.all()
    for r in comment_list:
        post_user = AuthUserprofile.objects.filter(user_id=r.post.user_id)
        comment_user = AuthUserprofile.objects.filter(user_id=r.user_id)
        r_json = {
            'post_nickname': post_user[0].nickname if post_user else '',
            'post_id': r.post_id, 
            'title': r.title,
            'nickname': comment_user[0].nickname if comment_user else '',
            'id': r.id,
            'content': r.content,
            'create_time': r.created_time.strftime('%Y-%m-%d')
        }
        content_list.append(r_json)
    common_json['list'] = content_list
    common_json['pages']['page'] = page
    common_json['pages']['recordsPerPage'] = psize
    common_json['pages']['totalRecord'] = total
    common_json['pages']['totalPage'] = (total - 1) / psize + 1
    return common_json

