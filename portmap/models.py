# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class WanIp(models.Model):
    w_ip = models.GenericIPAddressField(unique=True, verbose_name='WAN_IP')
    description = models.TextField(max_length=255, blank=True, null=True, verbose_name='备注')

    class Meta:
        permissions = (
            ('view_wanip', 'View WanIp'),
        )
        ordering = ["w_ip"]
        verbose_name = '公网地址管理'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'%s' % self.w_ip

    def __str__(self):
        return u'%s' % self.w_ip


class LanIp(models.Model):
    l_ip = models.GenericIPAddressField(verbose_name='LAN_IP')
    area = models.CharField(default='INSIDE', max_length=20, verbose_name='区域')
    status = models.NullBooleanField(default=True, choices=((True, '在用'), (False, '空闲'), (None, '未知')), verbose_name='状态')
    description = models.TextField(blank=True, null=True, verbose_name='详细信息')

    class Meta:
        permissions = (
            ('view_lanip', 'View LanIp'),
        )
        ordering = ["l_ip"]
        verbose_name = '内网地址管理'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'%s' % self.l_ip

    def __str__(self):
        return u'%s' % self.l_ip


class Maps(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='映射名')
    w_ip = models.ForeignKey(WanIp, related_name='WanIp_Set', verbose_name='WAN_IP')
    w_port = models.IntegerField(null=True, blank=True, verbose_name='WAN_PORT')
    l_ip = models.ForeignKey(LanIp, related_name='LanIp_Set', verbose_name='LAN_IP')
    l_port = models.IntegerField(null=True, blank=True, verbose_name='LAN_PORT')
    scripts = models.TextField(null=True, blank=True, verbose_name='创建脚本')
    map_user = models.CharField(null=True, blank=True, max_length=20, unique=True, verbose_name='用户')
    map_date = models.DateField(verbose_name='开通日期')
    description = models.TextField(null=True, blank=True, verbose_name='功能描述')

    class Meta:
        permissions = (
            ('view_maps', 'View maps'),
        )
        ordering = ['w_ip', 'w_port', 'l_ip', 'l_port']
        verbose_name = '端口映射管理'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'%s' % self.name

    def __str__(self):
        return u'%s' % self.name


class Agent(models.Model):
    name = models.CharField(max_length=20, verbose_name='名称')
    agent_ip = models.ForeignKey(LanIp, related_name='LanIp_Set_2', verbose_name='代理IP')
    agent_port = models.IntegerField(null=True, blank=True, verbose_name='代理端口')
    app_ip = models.ForeignKey(LanIp, related_name='LanIp_Set_3', verbose_name='应用IP')
    app_port = models.IntegerField(null=True, blank=True, verbose_name='应用端口')
    description = models.TextField(null=True, blank=True, verbose_name='描述')

    class Meta:
        permissions = (
            ('view_agent', 'View agent'),
        )
        ordering = ['name', 'agent_ip', 'agent_port', 'app_ip']
        verbose_name = '应用代理表'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'%s' % self.name

    def __str__(self):
        return u'%s' % self.name


class Vagent(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, verbose_name='代理名称')
    w_ip = models.GenericIPAddressField(verbose_name='公网地址')
    w_port = models.CharField(max_length=20, verbose_name='公网端口')
    agent_ip = models.GenericIPAddressField(verbose_name='代理地址')
    agent_port = models.CharField(max_length=20, verbose_name='代理端口')
    app_ip = models.CharField(max_length=20, verbose_name='应用地址')
    app_port = models.CharField(max_length=20, verbose_name='应用端口')
    description = models.TextField(verbose_name='描述信息')

    class Meta:
        managed = False
        # create view v_agent_map as (select `pa`.`id` AS `id`,`pa`.`name` AS `name`,`pw`.`w_ip` AS `w_ip`,`pm`.`w_port` AS `w_port`,`pl`.`l_ip` AS `agent_ip`,`pa`.`agent_port` AS `agent_port`,`pl2`.`l_ip` AS `app_ip`,`pa`.`app_port` AS `app_port`,`pa`.`description` AS `description` from ((((`portmap_agent` `pa` left join `portmap_lanip` `pl` on((`pa`.`agent_ip_id` = `pl`.`id`))) left join `portmap_lanip` `pl2` on((`pa`.`app_ip_id` = `pl2`.`id`))) left join `portmap_maps` `pm` on((`pa`.`agent_ip_id` = `pm`.`l_ip_id`))) left join `portmap_wanip` `pw` on((`pm`.`w_ip_id` = `pw`.`id`))) where (1 = 1)) ;
        db_table = 'v_agent_map'


# 银联专线
class BankTunnel(models.Model):
    name = models.CharField(max_length=20, verbose_name='专线名称')
    bank_ip = models.GenericIPAddressField(verbose_name='对端IP')
    local_ip = models.GenericIPAddressField(verbose_name='本端IP')
    bank_contact = models.CharField(null=True, blank=True, max_length=50, verbose_name='对端业务')
    local_contact = models.CharField(null=True, blank=True, max_length=50, verbose_name='本端业务')
    tech_contact = models.CharField(null=True, blank=True, max_length=50, verbose_name='技术调试')
    open_date = models.DateField(null=True, blank=True, verbose_name='开通时间')
    script = models.TextField(null=True, blank=True, verbose_name='创建脚本')
    description = models.TextField(null=True, blank=True, verbose_name='描述信息')

    class Meta:
        verbose_name = '专线管理'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'%s' % self.name

    def __str__(self):
        return u'%s' % self.name