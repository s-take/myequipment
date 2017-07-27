# coding: utf-8
from django.db import models

# Create your models here.
class User(models.Model):
    """ユーザー"""
    employee_no = models.CharField('社員番号', max_length=64,primary_key=True)
    name = models.CharField('氏名', max_length=256)

    def __unicode__(self):
        return self.name


class Equipment(models.Model):
    """備品"""
    barcode = models.CharField('バーコード', max_length=64, primary_key=True)
    name = models.CharField('品名', max_length=256)
    manage_no = models.CharField('資産管理番号', max_length=128)
    manage_user = models.CharField('管理者', max_length=256)
    comment = models.TextField('備考', blank=True)

    def __unicode__(self):
        return self.name


class Rental(models.Model):
    """貸出"""
    equipment = models.ForeignKey(Equipment)
    user = models.ForeignKey(User)
    processing = models.CharField('処理', max_length=64)
    created_at = models.DateTimeField('更新時間', auto_now_add=True)
    def is_rentaled(self):
        return self.processing == "rent"
    '''
    def get_equipment_name(self):
        return Equipment.objects.get(key=self.name)
    def get_equipment_manage_no(self):
        return Equipment.objects.get(key=self.manage_no)
    def get_equipment_manage_user(self):
        return Equipment.objects.get(key=self.manage_user)
    def get_equipment_comment(self):
        return Equipment.objects.get(key=self.comment)
    def get_user_name(self):
        return User.objects.get(key=self.name)
    '''
    def __unicode__(self):
        return self.equipment.name