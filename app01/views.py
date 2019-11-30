'''
@Author: kiwi
@Date: 2019-11-30 15:31:27
@LastEditors: kiwi
@LastEditTime: 2019-11-30 17:57:49
@Description: 描述
'''
from django.shortcuts import render, HttpResponse, redirect, reverse
from app01 import models
from app01.forms import RegForm
import hashlib



# Create your views here.
def login(request):
    error = ''
    if request.method== 'POST':
        username  = request.POST.get('username')
        password =  request.POST.get('password')
        md5 = hashlib.md5()
        md5.update(password.encode('utf-8'))
        password = md5.hexdigest()
        if models.UserProfile.objects.filter(username=username,password=password):
            return redirect('index')
        return render(request,'login.html',{'error':'账号或密码错误'})
    return render(request,'login.html')

def register(request):
    form_obj = RegForm()
    if request.method == 'POST':
        form_obj = RegForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            return redirect('login')
    return render(request,'register.html',{'form_obj':form_obj})


def index(request):
    return render(request,'layout.html')

def customer(request):
    all_customer = models.Customer.objects.all()
    return render(request,'customer.html',{'all_customer':all_customer})