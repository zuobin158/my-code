# -*- coding: utf-8 -*-
    
import logging
import md5
import copy
import json
import datetime
import requests

from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator
from django.db import transaction
from banner.models import Banner
from operation.dict_key import DICT_MAP
from django.core.cache import get_cache
from common.decorator import singleton
from operation.env import STATIC_SERVER


@singleton
class BannerService(object):

    def __init__(self, cache=None):
        self.cache = get_cache('default')

    def pack_banner(self, request):
        '''封装帖子信息数据
        '''
        page = int(request.GET.get('page',1))
        psize = int(request.GET.get('psize', 20))
        # banner名称
        name = request.GET.get('bannername', '') 
        is_active = request.GET.get('is_active', '') 
        q = Banner.objects.all()
        # 显示预览的数据
        q = q.filter(is_preview=True)
        q = q.order_by('order')
        if name:
            q = q.filter(name__contains=name)
        if is_active:
            q = q.filter(is_active=is_active)
        total = q.count()
        p = Paginator(q, psize)
        banner_list = p.page(page)

        common_json = copy.deepcopy(DICT_MAP['COMMON_LIST_JSON'])
        content_list = []
        for b in banner_list:
            r_json = self._pack_banner(b)
            content_list.append(r_json)
        common_json['statusCode'] = 1
        common_json['list'] = content_list
        common_json['pages']['page'] = page
        common_json['pages']['recordsPerPage'] = psize
        common_json['pages']['totalRecord'] = total
        common_json['pages']['totalPage'] = (total - 1) / psize + 1
        return common_json


    @staticmethod
    def _pack_banner(b):
        '''封装单个banner信息字段
        '''
        r_json = {
            'id': b.id,
            'name': b.name,
            'original': b.original,
            'thumbnail': b.thumbnail,
            'background': b.background,
            'background_image_width': b.background_image_width,
            'background_image_color': b.background_image_color,
            'page_url': b.location,
            'order': b.order,
            'is_active': b.is_active,
            'created_time': b.created_time.strftime('%Y-%m-%d') if b.created_time else '',
            'modified_time': b.modified_time.strftime('%Y-%m-%d') if b.modified_time else '',
            'update_user': b.update_user 
        }
        return r_json

    def save_or_update(self, request):
        '''新增和修改banner
        '''
        banner_id = request.POST.get('banner_id', '')
        name = request.POST.get('name', '')
        original = request.POST.get('original', '')
        thumbnail = request.POST.get('thumbnail', '')
        background = request.POST.get('background', '')
        background_image_width = request.POST.get('background_image_width', '')
        background_image_color = request.POST.get('background_image_color', '')
        location = request.POST.get('page_url', '')
        order = request.POST.get('order', '')
        update_user = ''
        if 'session_id' in request.COOKIES:
            session_id = request.COOKIES['session_id']
            update_user = self.cache.get(session_id)['username']
        if banner_id:
            ban = Banner.objects.filter(id=banner_id)
            ban = ban[0]
        else:
            ban = Banner()
            ban.order = 1
            ban.is_active = 1
        ban.is_preview = 1
        ban.name = name
        ban.original = original
        ban.thumbnail = thumbnail
        ban.background = background
        ban.background_image_width = background_image_width
        ban.background_image_color = background_image_color
        ban.location = location
        ban.update_user = update_user
        ban.save()
        return {'statusCode': 1}

    def get_banner(self, request):
        '''获取单个banner
        '''
        banner_id = request.GET.get('banner_id', '')
        b = Banner.objects.filter(id=banner_id)
        ban_json = {'statusCode': 0}
        if b:
            b = b[0]
            ban_json = self._pack_banner(b)
            ban_json['statusCode'] = 1
        return ban_json

    @transaction.commit_on_success(using='cms')
    def publish_banner(self):
        '''发布banner图
        '''
        # 1.复制新的banner草稿到线上banner
        draft_banner = Banner.objects.filter(is_preview=True,is_active=1)
        res_json = {'statusCode': 0, 'msg': ''}
        if draft_banner:
            # 2.删除老的线上banner
            old_banner = Banner.objects.filter(is_preview=False)
            old_banner.delete()
            for dra in draft_banner:
                ban = Banner()
                ban.name = dra.name
                ban.original = dra.original
                ban.thumbnail = dra.thumbnail
                ban.background = dra.background
                ban.background_image_width = dra.background_image_width
                ban.background_image_color = dra.background_image_color
                ban.location = dra.location
                ban.order = dra.order
                ban.is_active = 1
                ban.update_user = dra.update_user
                ban.is_preview = False
                ban.save()
                res_json['statusCode'] = 1
        else:
            res_json['statusCode'] = 0
            res_json['msg'] = '预览数据异常，请检查后重试'
        return res_json

    def get_preview_list(self):
        '''获取预览信息列表
        '''
        banner_list = Banner.objects.filter(is_active=1,is_preview=True).order_by('order')
        res_json = {'list':[], 'statusCode':0}
        res_list = []
        for b in banner_list:
            r_json = self._pack_banner(b)
            res_list.append(r_json)
        res_json['list'] = res_list
        res_json['statusCode'] = 1
        return res_json
        
    def init_banner_data(self):
        '''初始化数据，把banner数据复制一份到预览数据
        '''
        ban = Banner.objects.filter(is_preview=True)
        if ban:
            return {'statusCode':1, 'msg': 'preview data is already exist'}
        online_banner = Banner.objects.filter(is_preview=False)
        for dra in online_banner:
            ban = Banner()
            ban.name = dra.name
            ban.original = dra.original
            ban.thumbnail = dra.thumbnail
            ban.background = dra.background
            ban.background_image_width = dra.background_image_width
            ban.background_image_color = dra.background_image_color
            ban.location = dra.location
            ban.order = dra.order
            ban.is_active = dra.is_active
            ban.update_user = dra.update_user
            ban.is_preview = True
            ban.save()
        return {'statusCode':1, 'msg': 'success!'}

    def upload(self, request):
        '''上传图片到静态文件服务器
        '''
        pic = request.FILES['pic']
        url = STATIC_SERVER['PUBLIC_API']
        now = datetime.datetime.now()
        file_name = '{}{}'.format(now.strftime('%Y%m%d%H%M%S'), str(now.microsecond))
        static_file_url = DICT_MAP['STATIC_FILE_PATH']['banner'].format(file_name)
        upload_url = '{}{}'.format(url, static_file_url)
        files = {'file':pic.file.read()}
        r = requests.post(upload_url, files=files)
        res_url = json.loads(r.content)
        return {'statusCode':1, 'pic_url': res_url['url']}





