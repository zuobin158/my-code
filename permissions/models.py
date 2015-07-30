# -*- coding: utf-8 -*-

from django.db import models

class System(models.Model):
    '''子系统'''
    # 系统名称
    name = models.CharField(max_length=30)
    # 系统key 
    skey = models.CharField(max_length=50)
    # url
    url = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True, db_index=True)

class Resources(models.Model):
    '''资源模板'''
    # 资源名称
    name = models.CharField(max_length=30)
    # 子系统
    system_id = models.ForeignKey(System)
    ext_content = models.TextField(null=True)
    description = models.CharField(max_length=255, null=True)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True, db_index=True)

    def __unicode__(self):
        return self.name

class Group(models.Model):
    '''角色'''
    name = models.CharField(max_length=30)
    # 对应的资源集合
    resources = models.ManyToManyField(Resources)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True, db_index=True)

    def __unicode__(self):
        return self.name

class User(models.Model):
    '''用户'''
    name = models.CharField(max_length=30,unique=True)
    pwd = models.CharField(max_length=30)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    # 是否活跃用户1:活跃，0：非活跃
    is_active = models.CharField(max_length=1, default='1', db_index=True)
    is_super = models.CharField(max_length=2, default='0', db_index=True)
    real_name = models.CharField(max_length=50,null=True)
    # 所在角色
    groups = models.ManyToManyField(Group)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True, db_index=True)

    def __unicode__(self):
        return self.name

class Menu(models.Model):
    '''菜单'''
    # 菜单名称
    name = models.CharField(max_length=30)
    # 菜单key
    mkey = models.CharField(max_length=50)
    # 对应资源
    resource = models.ForeignKey(Resources)
    # url
    url = models.CharField(max_length=200)
    parent_id = models.CharField(max_length=11,null=True)
    order = models.IntegerField(max_length=11)
    created = models.DateTimeField(auto_now_add=True, db_index=True)
    modified = models.DateTimeField(auto_now=True, db_index=True)
    
