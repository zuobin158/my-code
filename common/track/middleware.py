# -*- coding: utf-8 -*-


import datetime
import hashlib
from django.core.cache import get_cache
from django.http import HttpResponse, HttpResponseRedirect
from operation.dict_key import DICT_MAP
from django.shortcuts import render_to_response


class TrackMiddleware(object):

    def __init__(self):

        self.cache = get_cache('default')

    def process_request(self, request):
        '''在django接收到请求后，在views执行前，用来验证用户是否登录
        '''
        session_id = self._check_session(request)
        flag = False
        if session_id and self.cache.has_key(session_id):
            content = self.cache.get(session_id)
            self.cache.set(session_id, content, timeout=DICT_MAP['SESSION_EXPIRE_TIME'])
            flag = True
        if request.path in ['/', '/login']:
            flag = True
        if not flag:
            return HttpResponseRedirect('/')

    def process_response(self, request, response):
        '''在views执行之后，用来保存sessionid到浏览器的Cookie中
        '''
        if not self._check_session(request):
            key = str(datetime.datetime.now())
            session_id = hashlib.md5(key).hexdigest()
            response.set_cookie('session_id', session_id)
        return response
    
    def _check_session(self, request):
        '''验证cookie中是否有session_id
        '''
        if 'session_id' in request.COOKIES:
            session_id = request.COOKIES['session_id']
            return session_id if session_id else ''
        return ''


