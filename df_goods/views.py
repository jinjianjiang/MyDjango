from django.shortcuts import render
from django.core.paginator import Paginator,Page
from .models import *
# Create your views here.

def index(request):
    typelist = TypeInfo.objects.all()
    type_0 = typelist[0].goodsinfo_set.order_by('-id')[0:4]
    type_01 = typelist[0].goodsinfo_set.order_by('-gclick')[0:4]

    type_1 = typelist[1].goodsinfo_set.order_by('-id')[0:4]
    type_11 = typelist[1].goodsinfo_set.order_by('-gclick')[0:4]

    type_2 = typelist[2].goodsinfo_set.order_by('-id')[0:4]
    type_21 = typelist[2].goodsinfo_set.order_by('-gclick')[0:4]

    type_3 = typelist[3].goodsinfo_set.order_by('-id')[0:4]
    type_31 = typelist[3].goodsinfo_set.order_by('-gclick')[0:4]

    type_4 = typelist[4].goodsinfo_set.order_by('-id')[0:4]
    type_41 = typelist[4].goodsinfo_set.order_by('-gclick')[0:4]

    type_5 = typelist[5].goodsinfo_set.order_by('-id')[0:4]
    type_51 = typelist[5].goodsinfo_set.order_by('-gclick')[0:4]

    if request.session.has_key('user_name'):
        uname = request.session['user_name']
    else:
        uname = ''

    context = {
        'type0': type_0, 'type01': type_01,
        'type1': type_1, 'type11': type_11,
        'type2': type_2, 'type21': type_21,
        'type3': type_3, 'type31': type_31,
        'type4': type_4, 'type41': type_41,
        'type5': type_5, 'type51': type_51,
        'uname': uname
    }

    return render(request, 'df_goods/index.html', context)


def list_handle(request, tid, pindex, sort):
    typeinfo = TypeInfo.objects.get(pk=int(tid))
    news = typeinfo.goodsinfo_set.order_by('-id')[0:2]
    if sort == '1':  # 按最新排序
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-id')
    if sort == '2': # 按价格排序
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gprice')
    if sort == '3': # 按热度排序
        goods_list = GoodsInfo.objects.filter(gtype_id=int(tid)).order_by('-gclick')
    paginator = Paginator(goods_list,10)
    page = paginator.page(int(pindex))
    context = {
        'page':page,
        'paginator':paginator,
        'typeinfo':typeinfo,
        'sort':sort,
        'news':news,
    }
    return render(request, 'df_goods/list.html', context)

def detail(request, id):
    commodity = GoodsInfo.objects.get(pk=int(id))
    commodity.gclick = commodity.gclick+1
    commodity.save()
    news = commodity.gtype.goodsinfo_set.order_by('-id')[0:2]
    context = {
        'commodity': commodity,
        'news': news,
        'id': id,
    }
    return render(request, 'df_goods/detail.html', context)