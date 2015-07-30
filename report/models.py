# -*- coding: utf-8 -*-


from django.db import models
from userprofile.models import AuthUser

class BbsReport(models.Model):
    COMMENT = 'comment'
    POST = 'post'
    object_type_choices = (
        (COMMENT, '评论'),
        (POST, '帖子'),
    )
    status_choices = (
        (2, '已忽略'),
        (1, '已隐藏'),
        (0, '未处理'),
    )
    reason_choices = (
        (1001, '广告或垃圾信息'),
        (1002, '内容含违规信息'),
        (1003, '不宜公开讨论'),
        (0, '其它'),
    )
    id = models.IntegerField(primary_key=True)
    object_type = models.CharField(max_length=30,choices=object_type_choices)
    object_id = models.IntegerField() 
    status = models.IntegerField(choices=status_choices)
    reason = models.IntegerField(choices=reason_choices)
    detail = models.CharField(max_length=255, blank=True)
    reporter = models.ForeignKey(AuthUser, unique=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField()
    class Meta:
        app_label = 'cms'
        db_table = u'bbs_report'
    

