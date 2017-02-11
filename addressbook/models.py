# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=50, verbose_name='公司名称')
    tel = models.CharField(max_length=20, null=True, blank=True, verbose_name='公司电话')
    website = models.CharField(max_length=50, null=True, blank=True, verbose_name='公司主页')
    address = models.CharField(null=True, blank=True, max_length=100, verbose_name='公司地址')
    comments = models.TextField(null=True, blank=True, verbose_name='备注')

    class Meta:
        ordering = ["name"]
        verbose_name = '公司信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'%s' % self.name

    def __str__(self):
        return u'%s' % self.name


class Persons(models.Model):
    name = models.CharField(max_length=50, verbose_name='姓名')
    sex = models.NullBooleanField(null=True, blank=True, choices=((True, '男'), (False, '女'), (None, '未知')), verbose_name='性别')
    dept = models.CharField(max_length=50, null=True, blank=True, verbose_name='部门')
    company = models.ForeignKey(Company, null=True, blank=True, verbose_name='公司')
    contact = models.CharField(max_length=150, null=True, blank=True, verbose_name='联系方式')
    comment = models.TextField(null=True, blank=True, verbose_name='备注')

    class Meta:
        ordering = ["dept", "name"]
        verbose_name = '人员信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'%s' % self.name

    @property
    def __str__(self):
        return u'%s' % self.name
