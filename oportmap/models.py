# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class OWanIp(models.Model):
    w_ip = models.CharField(max_length=20,  unique=True, verbose_name='WAN_IP')
    description = models.TextField(max_length=255, blank=True, null=True, verbose_name='备注')

    class Meta:
        permissions = (
            ('view_owanip', 'View OWanIp'),
        )
        ordering = ["w_ip"]
        verbose_name = '公网地址管理'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'%s' % self.w_ip

    def __str__(self):
        return u'%s' % self.w_ip


class OLanIp(models.Model):
    l_ip = models.CharField(max_length=20, verbose_name='LAN_IP')
    area = models.CharField(default='INSIDE', max_length=20, verbose_name='区域')
    status = models.NullBooleanField(default=True, choices=((True, '在用'), (False, '空闲'), (None, '未知')), verbose_name='状态')
    description = models.TextField(blank=True, null=True, verbose_name='详细信息')

    class Meta:
        permissions = (
            ('view_owanip', 'View OWanIp'),
        )
        ordering = ["l_ip"]
        verbose_name = '内网地址管理'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'%s' % self.l_ip

    def __str__(self):
        return u'%s' % self.l_ip


class OMaps(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='映射名')
    w_ip = models.ForeignKey(OWanIp, related_name='OWanIp_Set', verbose_name='WAN_IP')
    w_port = models.IntegerField(verbose_name='WAN_PORT')
    l_ip = models.ForeignKey(OLanIp, related_name='OLanIp_Set', verbose_name='LAN_IP')
    l_port = models.IntegerField(verbose_name='LAN_PORT')
    map_user = models.CharField(max_length=20, unique=True, verbose_name='用户')
    map_date = models.DateField(verbose_name='开通日期')
    description = models.TextField(verbose_name='功能描述')

    class Meta:
        permissions = (
            ('view_omaps', 'View OMaps'),
        )
        ordering = ['w_ip', 'w_port', 'l_ip', 'l_port']
        verbose_name = '端口映射表'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'%s' % self.name

    def __str__(self):
        return u'%s' % self.name
