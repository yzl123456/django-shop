# coding=utf-8
from django.db import models
from datetime import datetime
from tinymce.models import HTMLField

# 商品种类表


class GoodSort(models.Model):
    sortName = models.CharField(max_length=10)
    sortPic = models.ImageField(upload_to='uploads/')
    sortClass = models.CharField(max_length=20)  # 预留

    class Meta():
        db_table = 'goodsort'

    def __str__(self):
        return self.sortName


# 商品表


class Goods(models.Model):
    goodsName = models.CharField(max_length=30)
    goodsDesc = models.CharField(max_length=80)
    goodsPrice = models.DecimalField(max_digits=7, decimal_places=2)
    goodsDetail = HTMLField()
    imgPath = models.ImageField(upload_to='uploads/')
    saleCount = models.IntegerField(default=0)
    goodSort = models.ForeignKey('GoodSort')
    gPubdate = models.DateTimeField()
    extra = models.CharField(max_length=20, null=True, blank=True)  # 预留

    class Meta():
        db_table = 'goods'

    def __str__(self):
        return self.goodsName


# 商品评论


class GoodsComment(models.Model):
    userName = models.CharField(max_length=30)
    commentDate = models.DateTimeField()
    comment = HTMLField()
    goods = models.ForeignKey('Goods')
    extra = models.CharField(max_length=20, null=True, blank=True)  # 预留

    class Meta():
        db_table = 'goodscomment'

    def __str__(self):
        return self.userName

