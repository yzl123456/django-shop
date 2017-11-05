# coding=utf-8
from haystack import indexes
from goodslist.models import Goods


class GoodsIndex(indexes.SearchIndex, indexes.Indexable):
	text = indexes.CharField(document=True, use_template=False)

	def get_model(self):
		return Goods

	def index_queryset(self, using=None):
		print("---00")
		print(self.get_model().objects.all())
		return self.get_model().objects.all()