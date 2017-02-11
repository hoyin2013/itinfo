# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models

SERVICE_RANGE_CHOISE = {(1, '1年'), (2, '2年'), (3, '3年'), (4, '4年'), (5, '5年'), (6, '6年'), (7, '7年'), (8, '8年'), (0, '长期')}
USER_STATUS_CHOISE = {(1, '停用'), (2, '正常'), (3, '锁定')}
DBSERVER_POS_CHOISE = {(1, '东单机房'), (2, '中关村机房'), (3, '上海机房')}
FIRM_CHOISE = {(1, 'DELL'), (2, 'IBM'), (3, 'EMC')}


class Dbserver(models.Model):
    name = models.CharField(max_length=30, verbose_name='名称')
    ip = models.GenericIPAddressField(verbose_name='IP')
    pos = models.IntegerField(default=1, choices=DBSERVER_POS_CHOISE, verbose_name='位置')
    sn = models.CharField(null=True, blank=True, max_length=50, verbose_name='序列号')
    sid = models.CharField(null=True, blank=True, max_length=50, verbose_name='快速服务代码')
    firm = models.IntegerField(default=1, choices=FIRM_CHOISE, verbose_name='厂商')
    model = models.CharField(null=True, blank=True, max_length=30, verbose_name='型号')
    feature = models.TextField(null=True, blank=True, verbose_name='配置')
    buy_time = models.DateField(null=True, blank=True, verbose_name='购买时间')
    service_range = models.IntegerField(default=1, choices=SERVICE_RANGE_CHOISE, verbose_name='服务年限')
    comment = models.TextField(null=True, blank=True, verbose_name='备注')

    class Meta:
        ordering = ["name"]
        verbose_name = '生产服务器信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'%s' % self.name

    def __str__(self):
        return u'%s' % self.name


class Users(models.Model):
    dbserver = models.ForeignKey(Dbserver, null=True, blank=True, verbose_name='服务器')
    user = models.CharField(max_length=20, verbose_name='用户名')
    passwd = models.CharField(max_length=20, verbose_name='密码')
    tablespace = models.CharField(max_length=20, null=True, blank=True, verbose_name='表空间')
    status = models.IntegerField(choices=USER_STATUS_CHOISE, verbose_name='状态')
    business = models.CharField(null=True, blank=True, max_length=100, verbose_name='业务')
    created = models.DateField(null=True, blank=True, verbose_name='创建时间')
    comment = models.TextField(null=True, blank=True, verbose_name='备注')

    class Meta:
        ordering = ["user"]
        verbose_name = '生产数据库用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'%s' % self.business

    def __str__(self):
        return u'%s' % self.business


class Sysusers(models.Model):
    dbserver = models.ForeignKey(Dbserver, null=True, blank=True, verbose_name='服务器')
    name = models.CharField(max_length=20, verbose_name='名称')
    user = models.CharField(max_length=20, verbose_name='用户')
    passwd = models.CharField(max_length=20, verbose_name='密码')

    class Meta:
        ordering = ["dbserver"]
        verbose_name = '生产系统用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'%s' % self.name

    def __str__(self):
        return u'%s' % self.name


class Mysqluser(models.Model):
    dbserver = models.ForeignKey(Dbserver, verbose_name='服务器')
    name = models.CharField(max_length=20, verbose_name='用户名')
    passwd = models.CharField(max_length=20, verbose_name='密码')
    dbname = models.CharField(max_length=20, verbose_name='数据库名')
    business = models.CharField(null=True, blank=True, max_length=100, verbose_name='业务')
    comment = models.TextField(null=True, blank=True, verbose_name='备注')

    class Meta:
        ordering = ["dbserver"]
        verbose_name = '生产MYSQL用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'%s' % self.business

    def __str__(self):
        return u'%s' % self.business
