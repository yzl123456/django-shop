from django.contrib import admin
from .models import *
# Register your models here.
class GoodsAdmin(admin.ModelAdmin):
	list_display = ["id","goodsName","goodsPrice","imgPath"]

admin.site.register(Goods,GoodsAdmin)
admin.site.register(GoodSort)