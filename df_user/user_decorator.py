from django.shortcuts import redirect
from django.http import HttpResponseRedirect

def login(func):
    def login_fun(request, *args, **kwarges):
        if request.session.has_key('user_id'):
            return func(request, *args, **kwarges)
        else:
            red = HttpResponseRedirect('/user/login/')
            red.set_cookie('url', request.get_full_path())
            return red
    return login_fun