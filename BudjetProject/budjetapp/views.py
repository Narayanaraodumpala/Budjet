from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='login_signup')
def index(request):

    return render(request,'index.html')


def login_signup(request):
    error=False
    if request.method=='POST':
        usr=request.POST['user']
        pwd=request.POST['pwd']
        usr=authenticate(username=usr,password=pwd)
        if usr:
            login(request,usr)
            return redirect('home')
        else:
            error=True


    return render(request,'login_signup.html',{'error':error})


def signup(request):
    error = False
    if request.method == 'POST':
        usr = request.POST['user']
        pwd = request.POST['pwd']
        mob = request.POST['mob']
        img = request.FILES['img']
        add = request.POST['add']
        email = request.POST['email']
        usrdata=User.objects.filter(username=usr)
        if not usrdata:
            user=User.objects.create_user(username=usr,password=pwd,email=email)
            Userdetails.objects.create(auth_user=user,mobile=mob,image=img,address=add)
            return redirect('login_signup')
        else:
            error=True

    return render(request,'signup.html',{'error':error})


def logouttt(request):
    logout(request)
    return redirect('home')

@login_required(login_url='login_signup')
def about(request):
    return render(request,'about.html')


def experts(request):
    return render(request,'experts.html')


