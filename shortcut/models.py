# -*- coding:utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from datetime import datetime


class Shortcut(models.Model):
    user = models.ForeignKey(User, verbose_name='用户')
    name = models.CharField(max_length=50, verbose_name='名称')
    website = models.CharField(max_length=150, verbose_name='地址')
    add_date = models.DateTimeField(auto_now=True,  verbose_name='添加时间')
    show = models.BooleanField(default=True, choices=((True, '显示'), (False, '不显示')), verbose_name='显示')
    comment = models.TextField(null=True, blank=True, verbose_name='备注')

    class Meta:
        ordering = ["name"]
        verbose_name = '快捷链接'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'%s' % self.name

    def __str__(self):
        return u'%s' % self.name
