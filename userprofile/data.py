# -*- coding: utf-8 -*-
    
import logging
import md5
from django.http import HttpResponse, HttpResponseRedirect
from django.core.cache import get_cache
#from util.json_request import JsonResponse
from userprofile.models import (
        UserForbid,
        AuthUserprofile,
        AuthUser
    )

from operation.dict_key import DICT_MAP


def pack_user(user_list, page, psize, total):
    '''封装用户信息数据
    '''
    common_json = DICT_MAP['COMMON_LIST_JSON']
    content_list = []
    for u in user_list:
        is_forbid ='Y' if UserForbid.objects.filter(user_id=u.user_id) else 'N'
        aup = AuthUserprofile.objects.filter(user_id=u.user_id)
        has_avatar = 'N'
        if aup:
            has_avatar = 'Y' if aup[0].avatar else 'N'
        u_json = {
            'user_id': u.user_id,
            'nickname': u.nickname,
            'date_joined': u.user.date_joined.strftime('%Y-%m-%d'),
            'is_forbid': is_forbid,
            'has_avatar': has_avatar
        }
        content_list.append(u_json)
    common_json['list'] = content_list
    common_json['pages']['page'] = page
    common_json['pages']['recordsPerPage'] = psize
    common_json['pages']['totalRecord'] = total
    common_json['pages']['totalPage'] = (total - 1) / psize + 1
    return common_json





    
