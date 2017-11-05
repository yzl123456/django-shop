# coding=utf-8
from django.db import models
from datetime import datetime
from tinymce.models import HTMLField


# 用户表

class UserInfo(models.Model):
    uName = models.CharField(max_length=30)
    uPassword = models.CharField(max_length=40)
    uEmail = models.CharField(max_length=30)
    uPhoneNumber = models.CharField(max_length=15, default="空")
    uAddr = models.CharField(max_length=50, default="空")
    uRegDate = models.DateTimeField()
    isDelete = models.BooleanField(default=False)
    extra = models.CharField(max_length=20,null=True,blank=True) #预留

    class Meta():
        db_table = 'userinfo'

    def __str__(self):
        return self.uName

# 省市区表


# class AreaInfo(models.Model):
#     aTitle = models.CharField(max_length=20)
#     aParent = models.ForeignKey('self', null=True, blank=True)
#
#     class Meta():
#         db_table = 'areainfo'
#
#     def __str__(self):
#         return self.aTitle

# 地址信息表


class AddrInfo(models.Model):
    # aName = models.CharField(max_length=30) #账户名
    #aProvince = models.CharField(max_length=15)
    #aCity = models.CharField(max_length=15)
    #aDis = models.CharField(max_length=15, null=True, blank=True)
    aAddressee = models.CharField(max_length=20)  # 收信人
    aDetaAddr = models.CharField(max_length=30)
    #aPostCode = models.CharField(max_length=10, null=True, blank=True)
    aPhoneNumber = models.CharField(max_length=15)
    isDelete = models.BooleanField(default=False)
    aDefaultAddr = models.BooleanField(default=False)  # 默认地址
    extra = models.CharField(max_length=20,null=True,blank=True) #预留
    aUser = models.ForeignKey('UserInfo')

    class Meta():
        db_table = 'addrinfo'

    def __str__(self):
        return self.aPhoneNumber
