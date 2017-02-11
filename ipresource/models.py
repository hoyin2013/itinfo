# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Pos(models.Model):
    name = models.CharField(max_length=20,verbose_name='位置')
    desc = models.TextField(verbose_name='描述')

    class Meta:
        ordering = ["name"]
        verbose_name = '位置信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'%s' % self.name

    def __str__(self):
        return u'%s' % self.name


class Ipaddr(models.Model):
    ip = models.GenericIPAddressField(verbose_name='IP地址')
    vlan = models.IntegerField(verbose_name='vlan号')
    pos = models.ForeignKey(Pos, verbose_name='位置')
    func = models.CharField(max_length=20, verbose_name='功能描述')
    assign = models.BooleanField(verbose_name='是否分配')
    comment = models.TextField(verbose_name='备注')


    class Meta:
        ordering = ["ip"]
        verbose_name = 'IP信息'
        verbose_name_plural = verbose_name


    def __unicode__(self):
        return u'%s' % self.ip


    def __str__(self):
        return u'%s' % self.ip
