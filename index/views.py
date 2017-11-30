# coding=utf-8
from django.shortcuts import render
from django.http import *
from cart.models import *
from detail.models import *
from goodslist.models import *
from index.models import *
from registerLogin.models import *
from usercenter.models import *
import json
from usercenter import der
from django.core.urlresolvers import reverse
# 首页
# @der.login_yz
@der.login_name
def index(request,dic):
	# 拿到产品分类信息
	SortsMsg=GoodSort.objects.all()
	message=[]
	for sort in SortsMsg:
		message.append({'sort':sort,'goodMsgList':sort.goods_set.all().order_by('goodsName')[0:4],'goodOtherList':sort.goods_set.all().order_by('goodsName')[4:7]})
		
	print(message)
	dic=dict(dic,**{
		'message':message,
		})
	
	return render(request,'freshFruit/index.html',dic)

def loginOut(request):
	del request.session['name']
	return HttpResponseRedirect(reverse('index:indexPage'))
def search(request):
	keyword=request.GET.get('q')

	SortsMsg=GoodSort.objects.all()

	SortsMsg = GoodSort.objects.all()
	message = []
	for sort in SortsMsg:
		message.append({'sort': sort, 'goodMsgList': sort.goods_set.all().order_by('goodsName')[0:4],
						'goodOtherList': sort.goods_set.all().order_by('goodsName')[4:7]})

	goodslist=Goods.objects.filter(goodsName__icontains=keyword)
	print(goodslist)
	return render(request,"freshFruit/search.html",{"SortsMsg":SortsMsg,"goodMsgList":goodslist})



