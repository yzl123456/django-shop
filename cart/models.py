# coding=utf-8
from django.db import models
from datetime import datetime
from tinymce.models import HTMLField

class Cart(models.Model):
    goodsName = models.CharField(max_length=30)
    buyCount = models.IntegerField(default=1)
    isDelete = models.BooleanField(default=False)
    userCart = models.ForeignKey('usercenter.UserInfo')
    extra = models.CharField(max_length=20,null=True,blank=True) #预留

    class Meta():
        db_table = 'cart'

    def __str__(self):
        return self.goodsName


#最近浏览
class RecentSee(models.Model):
    goodsName=models.CharField(max_length=30)
    extra = models.CharField(max_length=20,null=True,blank=True) #预留
    user=models.ForeignKey('usercenter.UserInfo')
    class Meta():
        db_table='recentsee'
    def __str__(self):
        return self.goodsName

  

