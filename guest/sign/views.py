from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import login_required


# def index(request):
#     return render(request,"index.html")
# Create your views here.
# 登录动作
def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
        # if username == 'admin' and password == 'admin123':
            # return HttpResponse('login access!')
            response = HttpResponseRedirect('/event_manage/')
            # response.set_cookie('user', username, 3600)
            request.session['user']=username
            return response


        else:
            return render(request, 'index.html', {'error': 'username or password error!'})
    else:
        # return HttpResponse('error: username or password error!')
        return render(request, 'index.html')


# 发布会管理
@login_required
def event_manage(request):
    # username = request.COOKIES.get('user', '')
    username=request.session.get('user','')
    return render(request, 'event_manage.html', {"user": username})
