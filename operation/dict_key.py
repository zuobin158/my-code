# -*- coding: utf-8 -*-

DICT_MAP = {
    # cms管理后台地址
    'CMS_SYS_URL': 'http://192.168.9.189:7778/index?sessionid={}',    

    # 用户的session过期时间，即memcache缓存时间
    'SESSION_EXPIRE_TIME': 60 * 20,

    # 列表返回json格式
    'COMMON_LIST_JSON': {
        'statusCode': 0,
        'pages':{
            'page':1,
            'totalPage':1,
            'recordsPerPage':20,
            'totalRecord':0
        },  
        'list':[]
    },  
    # 帖子详情返回json格式
    'POST_DETAIL_JSON':{
        'statusCode': 0,
        'postTitle': '',
        'postBody': ''
    },
    # 操作返回json格式
    'OP_JSON':{
        'statusCode': 0,
        'msg': 'succeed'
    },
    # 静态文件存储路径
    'STATIC_FILE_PATH':{
        'banner': '/public_assets/xuetangx/banner/{}'
    
    },
    # 新用户默认pwd
    'DEFAULT_PWD': '000000'


}

