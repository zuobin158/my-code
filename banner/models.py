# -*- coding: utf-8 -*-


from django.db import models

class Banner(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128, unique=True)
    original = models.CharField(max_length=255, unique=True)
    thumbnail = models.CharField(max_length=255, blank=True)
    background = models.CharField(max_length=255)
    background_image_width = models.CharField(null=True, max_length=255)
    background_image_color = models.CharField(null=True, max_length=255)
    location = models.CharField(max_length=255)
    order = models.IntegerField(blank=True)
    is_active = models.IntegerField()
    created_time = models.DateTimeField(auto_now_add=True, db_index=True)
    modified_time = models.DateTimeField(auto_now=True, db_index=True)
    update_user = models.CharField(null=True, max_length=50)
    is_preview = models.BooleanField(default=True, db_index=True)
    class Meta:
        app_label = 'cms'
        db_table = u'homepage_banner'


