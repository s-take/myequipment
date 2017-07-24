from django.db import models

# Create your models here.
class User(models.Model):
    """ユーザー"""
    employee_no = models.CharField('社員番号', max_length=255)
    name = models.CharField('氏名', max_length=255)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    """備品"""
    name = models.CharField('品名', max_length=255)
    manage_no = models.CharField('管理番号', max_length=255)
    manage_user = models.CharField('管理者', max_length=255)
    comment = models.TextField('備考', blank=True)

    def __str__(self):
        return self.comment


class Rental(models.Model):
    """貸し出し状況"""
    user = models.ForeignKey(User, verbose_name='ユーザー', related_name='rentals')
    equipment = models.ForeignKey(Equipment, verbose_name='備品', related_name='rentals')
    last_rental_date = models.DateTimeField('最終貸出日')
    last_return_date = models.DateTimeField('最終返却日')

    def __str__(self):
        return self.name

    def is_returned(self):
        return self.last_rental_date.date() > self.last_return_date.date()


class Log(models.Model):
    """貸し出し履歴"""
    PROCESSING_CHOICES = (
        (u'Rental'),
        (u'Return'),
    )
    user = models.ForeignKey(User, verbose_name='ユーザー', related_name='rentals')
    equipment = models.ForeignKey(Equipment, verbose_name='備品', related_name='rentals')
    processing = models.CharField('処理', max_length=64, choices=PROCESSING_CHOICES)
    update_at = mmodels.DateTimeField('更新日')

    def __str__(self):
        return self.comment
