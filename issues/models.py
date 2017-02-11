# -*- coding:utf-8 -*-
from __future__ import unicode_literals

from django.db import models


DEPARTMENT_CHOISE = {(1, '运维部'), (2, '测试部'), (3, '结算部'), (4, '风控部'), (5, '产品部')}
UPDATE_TYPE_CHOISE = {(1, '正常变更'), (2, '紧急变更')}
OP_TYPE_CHOISE = {(1, '系统操作'), (2, '数据库操作'), (3, '混合操作')}


class Person(models.Model):
    name = models.CharField(max_length=50, verbose_name='姓名')
    dept = models.IntegerField(choices=DEPARTMENT_CHOISE, default=1, verbose_name='部门')
    mobile = models.CharField(max_length=50, null=True, blank=True, verbose_name='电话')
    email = models.EmailField(null=True, blank=True, verbose_name='邮箱')
    comment = models.TextField(null=True, blank=True, verbose_name='备注')

    class Meta:
        ordering = ["name"]
        verbose_name = '人员信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'%s' % self.name

    def __str__(self):
        return u'%s' % self.name


class System(models.Model):
    sname = models.CharField(max_length=100, verbose_name='系统名称')
    short_desc = models.CharField(max_length=100, verbose_name='系统简介')
    author = models.ForeignKey(Person, null=True, blank=True, verbose_name='作者')
    comment = models.TextField(null=True, blank=True, verbose_name='详细信息')

    class Meta:
        ordering = ["sname"]
        verbose_name = '系统信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'%s' % self.sname

    def __str__(self):
        return u'%s' % self.sname


class Event(models.Model):
    release = models.IntegerField(verbose_name='事件编号')
    title = models.CharField(max_length=100, verbose_name='标题')
    sponsor = models.ForeignKey(Person, related_name="sp_person",  verbose_name='发起者')
    sp_dept = models.IntegerField(choices=DEPARTMENT_CHOISE, default=5, verbose_name='发起部门')
    update_type = models.IntegerField(choices=UPDATE_TYPE_CHOISE, default=1, verbose_name='变更类型')
    project = models.ForeignKey(System, verbose_name='所属项目')
    operator = models.ForeignKey(Person, related_name="op_person", verbose_name='操作者')
    op_type = models.IntegerField(default=1, choices=OP_TYPE_CHOISE, verbose_name='操作类型')
    begin_time = models.DateTimeField(verbose_name='开始时间')
    end_time = models.DateTimeField(verbose_name='结束时间')

    class Meta:
        ordering = ["-begin_time"]
        verbose_name = '上线信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return u'%s' % self.release

    def __str__(self):
        return u'%s' % self.release
