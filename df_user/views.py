from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from hashlib import sha1
from .user_decorator import *
# Create your views here.


def register(request):
    return render(request, 'df_user/register.html')


def register_handle(request):
    uname = request.POST['user_name']
    pwd = request.POST['pwd']
    cpwd = request.POST['cpwd']
    email = request.POST['email']
    # 判断两次密码是否一样
    if pwd != cpwd:
        return redirect('/user/register')
    # 对提交的密码进行加密
    s1 = sha1()
    s1.update(pwd.encode('utf-8'))
    pwd_hash = s1.hexdigest()
    # 创建model对象
    user = UserInfo()
    user.u_name = uname
    user.u_pwd = pwd_hash
    user.u_email = email
    user.save()
    # 注册成功后转到登录页面
    return redirect('/user/login')
# 返回登录页面
def user_login(request):
    uname = request.COOKIES.get('uname','') # 如果之前有记住用户名，那么在登录框中显示cookies中记录的用户名
    context = {'title':'用户登录','error_name':0,'error_pwd':0,'uname':uname}
    return render(request, 'df_user/login.html',context)
# 返回info页面
@login
def info(request):
    u_name = request.session['user_name']
    u_email = UserInfo.objects.get(pk=request.session['user_id']).u_email
    context = {'uname': u_name, 'uemail':u_email}
    return render(request, 'df_user/user_center_info.html', context)
# 返回site页面
@login
def site(request):
    user = UserInfo.objects.get(pk=request.session['user_id'])
    if request.method == 'POST':
        user.u_delivery = request.POST['u_delivery']
        user.u_address = request.POST['u_address']
        user.u_post = request.POST['u_post']
        user.u_phone = request.POST['u_phone']
        user.save()
    context = {'user':user}
    return render(request, 'df_user/user_center_site.html', context)
@login
def order(request):
    return render(request, 'df_user/user_center_order.html')

# 登录信息处理
def login_handle(request):
    login_name = request.POST['username']
    login_pwd = request.POST['pwd']
    jizhu = request.POST.get('jizhu', 0)
    user_find = UserInfo.objects.filter(u_name=login_name)
    if len(user_find) == 1:
        s1 = sha1()
        s1.update(login_pwd.encode('utf-8'))
        if s1.hexdigest() == user_find[0].u_pwd:
            url = request.COOKIES.get('url', '/')
            red = HttpResponseRedirect(url)
            if jizhu != 0: # 如果选择记住用户名，那么向用户cookies中写入用户名
                red.set_cookie('uname', login_name)
            else:
                red.set_cookie('uname', '', max_age=-1)
            request.session['user_id'] = user_find[0].id
            request.session['user_name'] = login_name
            return red
        else:
            context = {'title':'用户登录','error_name':0,'error_pwd':1,'uname':login_name,'upwd':login_pwd}
            return render(request, 'df_user/login.html', context)
    else:
        context = {'title':'用户登录','error_name':1,'error_pwd':0,'uname':login_name,'upwd':login_pwd}
        return render(request, 'df_user/login.html', context)

# 退出
@login
def logout(request):
    request.session.flush()
    return redirect('/')


# 判断用户名是否存在
def register_exist(request):
    uname = request.GET.get('uname') # register.js中调用，通过url传递参数
    count = UserInfo.objects.filter(u_name=uname).count()
    return JsonResponse({'count':count})
