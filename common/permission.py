# -*- coding: utf-8 -*-


from lms_cms.dict_key import DICT_MAP

cache = get_cache('default')

def check_login():                                                                                                                  
    '''子系统中的检查登录状态的修饰器
    '''
    def wrapper(func):
        def check_login_warpper_func(request, *args, **kwargs):
            if 'session_id' in request.session:
                if cache.has_key(request.session['session_id']):
                    return func(request, *args, **kwargs)
            return HttpResponseRedirect(DICT_MAP['LOGIN_HOST'])
        return check_login_warpper_func
    return wrapper
