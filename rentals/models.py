# coding: utf-8
from django.db import models

# Create your models here.
class User(models.Model):
    """ユーザー"""
    employee_no = models.CharField('社員番号', max_length=255,primary_key=True)
    name = models.CharField('氏名', max_length=255)

    def __unicode__(self):
        return self.name


class Equipment(models.Model):
    """備品"""
    barcode = models.CharField('バーコード', max_length=255, primary_key=True)
    name = models.CharField('品名', max_length=255)
    manage_no = models.CharField('資産管理番号', max_length=255)
    manage_user = models.CharField('管理者', max_length=255)
    comment = models.TextField('備考', blank=True)

    def __unicode__(self):
        return self.name


class Rental(models.Model):
    """貸出"""
    equipment = models.ForeignKey(Equipment, verbose_name='備品', related_name='rentals')
    user = models.ForeignKey(User, verbose_name='ユーザー', related_name='rentals')
    processing = models.CharField('処理', max_length=64)
    created_at = models.DateTimeField('更新時間', auto_now_add=True)

    def __unicode__(self):
        return self.equipment.name