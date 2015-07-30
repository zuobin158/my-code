# -*- coding: utf-8 -*-


from django.db import models
from userprofile.models import AuthUser

class Notification(models.Model):
    '''站内信
    '''
    #id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(AuthUser)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=50)
    status = models.IntegerField()
    meta = models.TextField()
    class Meta:
        app_label = 'cms'
        db_table = u'notification_notification'


class NotificationMsg(models.Model):
    '''系统站内信
    '''
    #id = models.IntegerField(primary_key=True)
    content = models.TextField()
    outlink = models.CharField(null=True,max_length=1000)
    title = models.CharField(null=True,max_length=500)
    link_remark = models.CharField(null=True,max_length=500)
    update_user = models.CharField(null=True,max_length=50)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    class Meta:
        app_label = 'cms'
        db_table = u'notification_msg'


class NotifyMsg(models.Model):
    '''系统站内信和站内信的对应关系，一个系统站内信对应多条站内信，多个人的。
    '''
    #id = models.IntegerField(primary_key=True)
    mid = models.IntegerField()
    nid = models.IntegerField()
    class Meta:
        app_label = 'cms'
        db_table = u'notify_msg'


