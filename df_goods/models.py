from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class TypeInfo(models.Model):
    ttitle = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)

    class Meta():
        db_table = 'typeinfo'  # 实现改变表的名字

    def __str__(self):
        return self.ttitle

class GoodsInfo(models.Model):
    gtitle = models.CharField(max_length=20)  # 名称
    gpic = models.ImageField(upload_to='df_goods')  # 图片
    gprice = models.DecimalField(max_digits=5, decimal_places=2)  # 价格
    isDelete = models.BooleanField(default=False)  # 逻辑删除
    gunit = models.CharField(max_length=20, default='500g')  # 单位
    gclick = models.IntegerField()  # 点击量
    gabstract = models.CharField(max_length=100)  # 简介
    grepertory = models.IntegerField()  # 库存
    gcontent = HTMLField()  # 详细信息
    gtype = models.ForeignKey('TypeInfo')
   # gadv = models.BooleanField(default=False)

    class Meta():
        db_table = 'goodsinfo'  # 实现改变表的名字

    def __str__(self):
        return self.gtitle