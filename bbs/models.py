# -*- coding: utf-8 -*-


from django.db import models
from userprofile.models import AuthUser

class BbsCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    name = models.CharField(max_length=765, unique=True)
    slug = models.CharField(max_length=765, unique=True)
    icon = models.CharField(max_length=3072, blank=True)
    order = models.IntegerField(null=True, blank=True)
    class Meta:
        app_label = 'cms'
        db_table = u'bbs_category'


class BbsTag(models.Model):
    id = models.IntegerField(primary_key=True)
    created_time = models.DateTimeField(auto_now_add=True)
    modified_time = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)
    slug = models.CharField(null=True, max_length=255)
    class Meta:
        app_label = 'cms'
        db_table = u'bbs_tag'



class BbsPost(models.Model):
    status_choices = ( 
        ('0', '否'),
        ('1', '是'),
    )
    id = models.IntegerField(primary_key=True)
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    title = models.CharField(max_length=765)
    content = models.TextField()
    html_content = models.TextField()
    status = models.IntegerField(choices=status_choices)
    hot_count = models.IntegerField()
    category = models.ForeignKey(BbsCategory)
    promotion_order = models.IntegerField(null=True, blank=True)
    user = models.ForeignKey(AuthUser)
    class Meta:
        app_label = 'cms'
        db_table = u'bbs_post'

class BbsPostTag(models.Model):
    id = models.IntegerField(primary_key=True)
    post = models.ForeignKey(BbsPost)
    tag = models.ForeignKey(BbsTag)
    class Meta:
        app_label = 'cms'
        db_table = u'bbs_post_tags'


class BbsComment(models.Model):
    id = models.IntegerField(primary_key=True)
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()
    title = models.CharField(max_length=765)
    content = models.TextField()
    html_content = models.TextField()
    status = models.IntegerField()
    post = models.ForeignKey(BbsPost)
    reference_id = models.IntegerField()
    user = models.ForeignKey(AuthUser)
    reply_to = models.ForeignKey(AuthUser)
    class Meta:
        app_label = 'cms'
        db_table = u'bbs_comment'

