# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


SERVICE_RANGE_CHOISE = {(1, '1年'), (2, '2年'), (3, '3年'), (4, '4年'), (5, '5年'), (6, '6年'), (7, '7年'), (8, '8年'), (0, '长期')}
DBSERVER_POS_CHOISE = {(1, '生产机房'), (2, '测试机房'), (3, '上海灾备机房'), (4, '中关村机房'), (5, '生产新机房')}
ZONE_CHOISE ={('I', 'INSIDE'), ('O', 'OUTSIDE'), ('D', 'DMZ')}
SERVER_TYPE_CHOISE = {(1, '实体机'), (2, '虚拟机')}
MANU_CHOISE = {(1, 'Dell'), (2, 'IBM'), (3, 'EMC')}


class Server(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name=u'服务器名称')
    ip = models.CharField(max_length=20, blank=True, null=True, verbose_name='服务器IP')
    ext_ip = models.TextField(blank=True, null=True, verbose_name='其他IP')
    zone = models.CharField(max_length=5, blank=True, null=True, choices=ZONE_CHOISE, verbose_name='网络区域')
    sn = models.CharField(max_length=255, blank=True, null=True, verbose_name='编号')
    sid = models.CharField(max_length=255, blank=True, null=True, verbose_name='服务代码')
    manufacturer = models.IntegerField(choices=MANU_CHOISE, blank=True, null=True, verbose_name='品牌')
    mod = models.CharField(max_length=255, blank=True, null=True, verbose_name='型号')
    type = models.IntegerField(choices=SERVER_TYPE_CHOISE, blank=True, null=True, verbose_name='机器类型')
    feature = models.TextField(null=True, blank=True, verbose_name='配置')
    buy_date = models.DateField(blank=True, null=True, verbose_name='购买时间')
    contact = models.CharField(max_length=25, blank=True, null=True, verbose_name='联系人')
    factory_phone = models.CharField(max_length=25, blank=True, null=True, verbose_name='联系电话')
    service_range = models.IntegerField( choices=SERVICE_RANGE_CHOISE, verbose_name='保修')
    cabinet = models.CharField(max_length=20, blank=True, null=True, verbose_name='机柜号')
    idc = models.IntegerField(default=1, choices=DBSERVER_POS_CHOISE, verbose_name='机房')
    comment = models.TextField(blank=True, null=True, verbose_name='备注')

    class Meta:
        ordering = ["ip"]
        verbose_name = '应用服务器信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'%s' % self.ip

    def __str__(self):
        return u'%s' % self.ip


class App(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='应用名称')
    language = models.CharField(max_length=20, blank=True, null=True, verbose_name='开发语言')
    function = models.CharField(max_length=255, blank=True, null=True, verbose_name='功能')
    teams = models.CharField(max_length=255, blank=True, null=True, verbose_name='开发团队')
    dev_time = models.DateField(blank=True, null=True, verbose_name='开发时间')
    contact = models.CharField(max_length=255, blank=True, null=True, verbose_name='联系人')
    comment = models.TextField(blank=True, null=True, verbose_name='详细说明')

    class Meta:
        ordering = ["name"]
        verbose_name = '应用信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'%s' % self.name

    def __str__(self):
        return u'%s' % self.name


class Deploy(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='部署名称')
    server = models.ForeignKey(Server, verbose_name='部署服务器')
    app = models.ForeignKey(App, verbose_name='应用名称')
    paths = models.CharField(max_length=255, blank=True, null=True,  verbose_name='部署路径')
    users = models.CharField(max_length=255, blank=True, null=True,  verbose_name='系统用户')
    ports = models.IntegerField(blank=True, null=True, verbose_name='端口号')
    author = models.CharField(max_length=255, blank=True, null=True, verbose_name='部署人')
    dtime = models.DateField(blank=True, null=True, verbose_name='部署时间')
    documents = models.FileField(upload_to='./deploy', null=True, blank=True, verbose_name='部署文档')

    class Meta:
        ordering = ["name"]
        verbose_name = '部署信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'%s' % self.name

    def __str__(self):
        return u'%s' % self.name


class Business(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='业务名称')
    description = models.CharField(max_length=255, null=True, blank=True, verbose_name='业务简介')
    contacts = models.CharField(max_length=255, blank=True, null=True, verbose_name='业务负责人')
    ol_date = models.DateField(blank=True, null=True, verbose_name='上线时间')
    deploys = models.ManyToManyField(Deploy, verbose_name='部署')
    details = models.TextField(null=True, blank=True, verbose_name='详情')
    annex = models.FileField(null=True, blank=True, verbose_name='附件')

    # 显示ManyToMany域
    def deploy_list(self):
        return ','.join([a.name for a in self.deploys.all()])

    deploy_list.short_description = '业务系统列表'

    class Meta:
        ordering = ["name"]
        verbose_name = '业务信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'%s' % self.name

    def __str__(self):
        return u'%s' % self.name
