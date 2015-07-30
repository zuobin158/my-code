# -*- coding: utf-8 -*-
    
import logging
import md5
from django.http import HttpResponse, HttpResponseRedirect
from django.core.cache import get_cache
from django.core.paginator import Paginator
from userprofile.models import (
        UserForbid,
        AuthUserprofile,
        AuthUser
    )
from report.models import BbsReport
from bbs.models import BbsPost, BbsComment
from operation.dict_key import DICT_MAP


def pack_report(request):
    '''封装举报信息数据
    '''
    page = int(request.GET.get('page',1))
    psize = int(request.GET.get('psize', 20))
    # 帖子ID
    post_id = request.GET.get('post_id', '') 
    # 评论ID
    comment_id = request.GET.get('comment_id', '') 
    # 举报人昵称
    reporter_nickname = request.GET.get('reporter_nickname', '') 
    # 被举报人昵称
    reportered_nickname = request.GET.get('reportered_nickname', '') 
    # 举报类型
    object_type = request.GET.get('object_type', '') 
    # 举报原因
    reason = request.GET.get('reason', '') 
    # 举报时间开始
    create_time_start = request.GET.get('create_time_start', '') 
    # 举报时间结束
    create_time_end = request.GET.get('create_time_end', '') 
    # 状态
    status = request.GET.get('status', '') 
    # 关键字
    keywords = request.GET.get('keywords', '')
    q = BbsReport.objects.all()
    q = q.order_by('-created_time')
    if post_id:
        q = q.filter(object_id=post_id,object_type='post')
    if comment_id:
        q = q.filter(object_id=comment_id,object_type='comment')
    if reporter_nickname:
        users = AuthUserprofile.objects.filter(nickname__contains=reporter_nickname)    
        uids = []
        if users:
            uids = [u.user_id for u in users]
        q = q.filter(reporter_id__in=uids)
    if reportered_nickname:
        users = AuthUserprofile.objects.filter(nickname__contains=reportered_nickname)    
        uids = []
        if users:
            uids = [u.user_id for u in users]
        bbp = BbsPost.objects.filter(user_id__in=uids)
        bbc = BbsComment.objects.filter(user_id__in=uids)
        # 帖子
        poids = [p.id for p in bbp]
        q_bbp = q.filter(object_id__in=poids,object_type='post')
        # 评论
        coids = [p.id for c in bbc]
        q_bbc = q.filter(object_id__in=coids,object_type='comment') 
        q = q_bbp | q_bbc
    if object_type:
        q = q.filter(object_type=object_type)
    if reason:
        q = q.filter(reason=reason)
    if create_time_start:
        q = q.filter(created_time__gte=create_time_start)
    if create_time_end:
        create_time_end += ' 23:59:59'
        q = q.filter(created_time__lte=create_time_end)
    if status:
        q = q.filter(status=status)
    total = q.count()                                                                                                                        
    p = Paginator(q, psize)
    report_list = p.page(page)

    common_json = DICT_MAP['COMMON_LIST_JSON']
    content_list = []
    for r in report_list:
        aup = AuthUserprofile.objects.filter(user_id=r.reporter_id)
        bp = ''
        if r.object_type == 'post':
            bp = BbsPost.objects.filter(id=r.object_id)
        if r.object_type == 'comment':
            bp = BbsComment.objects.filter(id=r.object_id)
        reported = ''
        if bp:
            reported = AuthUserprofile.objects.filter(user_id=bp[0].user_id)

        r_json = {
            'id': r.id,
            'reportDate': r.created_time.strftime('%Y-%m-%d'),
            'type': r.get_object_type_display(),
            'reason': r.get_reason_display(),
            'reporter': aup[0].nickname if aup else '',
            'reported': reported[0].nickname if reported else '',
            'postId': r.object_id if r.object_type=='post' else '',
            'postTitle': bp[0].title if bp and r.object_type=='post' else '',
            'commentId': r.object_id if r.object_type=='comment' else '',
            'commentContent': bp[0].content if bp and r.object_type=='comment' else '',
            'status': r.get_status_display()
        }
        content_list.append(r_json)
    common_json['list'] = content_list
    common_json['pages']['page'] = page
    common_json['pages']['recordsPerPage'] = psize
    common_json['pages']['totalRecord'] = total
    common_json['pages']['totalPage'] = (total - 1) / psize + 1
    return common_json


def pack_post_detail(request):
    '''封装帖子详情
    '''
    post_id = request.GET.get('post_id', '')
    bp = BbsPost.objects.filter(id=post_id)
    common_json = DICT_MAP['POST_DETAIL_JSON']
    if bp:
       common_json['postTitle'] = bp[0].title
       common_json['postBody'] = bp[0].content
    return common_json

def update_report_status(request):
    '''修改举报信息状态
    '''
    report_id = request.GET.get('reportId', '')
    action = request.GET.get('action', '')
    br = BbsReport.objects.filter(id=report_id)
    if br:
        status = ''
        if action == 'hide':
            status = 1
            _update_bbs_info(br[0])
        if action == 'ignore':
            status = 2
        br[0].status = status 
        br[0].save()
        return {'statusCode': 1}
    return {'statusCode': 0}

def _update_bbs_info(report):
    '''修改评论或帖子的状态
    '''
    obj = ''
    if report.object_type == BbsReport.COMMENT:
        obj = BbsComment.objects.filter(id=report.object_id)
    if report.object_type == BbsReport.POST:
        obj = BbsPost.objects.filter(id=report.object_id)
    if obj:
        obj = obj[0]
        obj.status = -1
        obj.save()



