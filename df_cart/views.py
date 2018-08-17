from django.shortcuts import render, redirect
from django.http import JsonResponse
from df_user import user_decorator
from .models import *

# Create your views here.

@user_decorator.login
def cart(request):
    uid = request.session['user_id']
    carts = CartInfo.objects.filter(user_id=uid) # 读取用户购物车信息
    context = {'page_name':1, 'carts':carts}
    return render(request, 'df_cart/cart.html', context)


@user_decorator.login
def add(request, gid, count):
    uid = request.session['user_id']
    gid = int(gid)
    count = int(count)
    # 判断购物车中是否已经有此商品
    carts = CartInfo.objects.filter(user_id=uid, goods_id=gid)
    if len(carts)>=1:
        cart = carts[0]
        cart.count = cart.count+count
    else:
        cart = CartInfo()
        cart.user_id = uid
        cart.goods_id = gid
        cart.count = count
    cart.save()

    return redirect('/cart/')