# -*- coding: utf-8 -*-
# Django settings for operation project.

import sys
import os
import json

DEBUG = True
TEMPLATE_DEBUG = DEBUG

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

LOG_PATH = '/var/log/operation/all.log'

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

# 数据库路由规则
DATABASE_ROUTERS = ['operation.router.DBRouter']


# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.4/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['*',]

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'Asia/Shanghai'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en_us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = os.path.join(os.path.dirname(os.path.dirname(__file__)),'static').replace('\\','/')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    #'/edx/app/edxapp/operation/operation/static',
    PROJECT_ROOT + '/dev_static',
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = '2#3x9d-6ga+8^5!lg3*a!%9zst+f(1s10+r4w+$)2xrj!oa788'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'operation.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'operation.wsgi.application'

PROJECT_PATH = os.path.dirname(os.path.dirname(__file__))
sys.path.append(PROJECT_PATH + '/common')

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    #PROJECT_PATH + '/operation/templates',
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
    # 权限管理
    'permissions',
    'track',
    'per_resource',
    'per_user',
    'system',
    'group',
    'menu',
    'userprofile',
    'report',
    'bbs',
    'comment',
    'banner',
    'notification',
    'gunicorn',

)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.


LOGGING = { 
    'version': 1,
    'disable_existing_loggers': False,
    'formatters':{
        'standard': {
            'format': '%(asctime)s [%(name)s] [%(module)s:%(funcName)s] [%(levelname)s]- %(message)s'
        }   
    },  
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }   
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'outfile': {
            'level':'INFO',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': LOG_PATH,
            'maxBytes': 1024*1024*5,
            'backupCount': 5,  
            'formatter':'standard',
        },
        'console':{
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
    },  
    'loggers': {
        '''
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level':'DEBUG',
        },
        '''
        'django': {
            'handlers': ['console', 'outfile'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins', 'console', 'outfile'],
            'level': 'ERROR',
            'propagate': True,
        },
        'permissions': {
            'handlers': ['outfile', 'console'],
            'level': 'INFO',
            'propagate': True 
        },
        'bbs': {
            'handlers': ['outfile', 'console'],
            'level': 'INFO',
            'propagate': True 
        },
        'comment': {
            'handlers': ['outfile', 'console'],
            'level': 'INFO',
            'propagate': True 
        },
        'userprofile': {
            'handlers': ['outfile', 'console'],
            'level': 'INFO',
            'propagate': True 
        },
        'report': {
            'handlers': ['outfile', 'console'],
            'level': 'INFO',
            'propagate': True 
        },
        'banner': {
            'handlers': ['outfile', 'console'],
            'level': 'INFO',
            'propagate': True 
        },
        'notification': {
            'handlers': ['outfile', 'console'],
            'level': 'INFO',
            'propagate': True 
        },
        'per_user': {
            'handlers': ['outfile', 'console'],
            'level': 'INFO',
            'propagate': True 
        },
        'group': {
            'handlers': ['outfile', 'console'],
            'level': 'INFO',
            'propagate': True 
        },
        'menu': {
            'handlers': ['outfile', 'console'],
            'level': 'INFO',
            'propagate': True 
        },
        'per_resource': {
            'handlers': ['outfile', 'console'],
            'level': 'INFO',
            'propagate': True 
        }
    }
}




MIDDLEWARE_CLASSES += (
    'track.middleware.TrackMiddleware',

)

APPEND_SLASH = False

# ldap conf
# ldap服务器地址
LDAPPATH = 'ldap://xxxx'
# 根目录
BASE_DN = 'DC=aaaa,DC=bbbb,DC=com'
# ldap服务器用户名
LDAPUSER = 'xxxx'
# ldap服务器密码
LDAPPASS = 'xxxx'
