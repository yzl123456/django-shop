# coding=utf-8
from django.db import models
from datetime import datetime
from tinymce.models import HTMLField



# 订单表


class Orders(models.Model):
    
    isFinish = models.BooleanField(default=False)
    isDelete = models.BooleanField(default=False)
    orderTime = models.DateTimeField()
    orderNumber = models.CharField(max_length=20,null=True,blank=True) #预留
    userOrder = models.ForeignKey('usercenter.UserInfo')
    addr=models.IntegerField(default=0)
    class Meta():
        db_table = 'orders'

    def __str__(self):
        return self.orderNumber
#订单详细表
class OrderDetail(models.Model):
    goodsName = models.CharField(max_length=30)
    goodsPrice = models.DecimalField(max_digits=7, decimal_places=2)
    buyCount = models.IntegerField()
    orders_id = models.ForeignKey('Orders')
    good_id = models.ForeignKey('goodslist.Goods')

    class Meta():
        db_table = 'orderdetail'

    def __str__(self):
        return self.goodsName



  

