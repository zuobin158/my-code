# -*- coding: utf-8 -*-


from django.db import models

class AuthUser(models.Model):
    '''线上用户表
    '''
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=90, unique=True)
    first_name = models.CharField(max_length=90)
    last_name = models.CharField(max_length=90)
    email = models.CharField(max_length=225, unique=True, blank=True)
    password = models.CharField(max_length=384)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    is_superuser = models.IntegerField()
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField()
    class Meta:
        app_label = 'cms'
        db_table = u'auth_user'

class AuthUserprofile(models.Model):
    '''用户扩展信息表
    '''
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser, unique=True)
    name = models.CharField(max_length=255)
    language = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    meta = models.TextField()
    courseware = models.CharField(max_length=255)
    gender = models.CharField(max_length=18, blank=True)
    mailing_address = models.TextField(blank=True)
    year_of_birth = models.IntegerField(null=True, blank=True)
    level_of_education = models.CharField(max_length=18, blank=True)
    goals = models.TextField(blank=True)
    allow_certificate = models.IntegerField()
    country = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    district = models.CharField(max_length=255, blank=True)
    zip_code = models.CharField(max_length=45, blank=True)
    telephone_number = models.CharField(max_length=93, blank=True)
    last_login_ip = models.CharField(max_length=45, blank=True)
    nickname = models.CharField(max_length=255, unique=True, blank=True)
    phone_number = models.CharField(max_length=150, unique=True, blank=True)
    avatar = models.CharField(max_length=255)
    unique_code = models.CharField(max_length=60, unique=True, blank=True)
    class Meta:
        app_label = 'cms'
        db_table = u'auth_userprofile'

class UserForbid(models.Model):
    forbid_choices = (
        (1, 'bbs_banned'),
    )
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser, unique=True)
    report_count = models.IntegerField()
    forbid = models.IntegerField(choices=forbid_choices)
    remark = models.CharField(max_length=200, unique=True, blank=True)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField()
    class Meta:
        app_label = 'cms'
        db_table = u'user_forbid'
    

