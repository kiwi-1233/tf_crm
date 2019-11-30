from django.shortcuts import render, HttpResponse, redirect, reverse
from app01 import models
import hashlib
from app01.forms import RegForm


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))
        password = md5.hexdigest()
        if models.UserProfile.objects.filter(username=username, password=password, is_active=True):
            return HttpResponse('登录成功')
        return render(request, 'login.html', {'error': '用户名或密码错误'})

    return render(request, 'login.html')


def register(request):
    form_obj = RegForm()
    if request.method == 'POST':
        form_obj = RegForm(request.POST)
        if form_obj.is_valid():
            # 插入数据库
            # print(form_obj.cleaned_data)
            # models.UserProfile.objects.create(**form_obj.cleaned_data)
            form_obj.save()
            return redirect(reverse('login'))

    return render(request, 'register.html', {'form_obj': form_obj})


def customer(request):
    all_customer = models.Customer.objects.all()
    return render(request,'customer.html',{'all_customer':all_customer})