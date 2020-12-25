from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import *
from django.contrib.auth import authenticate,logout,login
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
@login_required(login_url='login_signup')
def index(request):

    return render(request,'index.html',{'experts':Expert.objects.all()})


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

@login_required(login_url='login_signup')
def experts(request):
    return render(request,'experts.html')

@login_required(login_url='login_signup')
def user_dashboard(request):
    mde= Userdetails.objects.filter(auth_user=request.user)
    return render(request,'user_dashboard.html',{'profile':mde})

@login_required(login_url='login_signup')
def expert_consultants(request):

    return render(request,'expert_consultants.html',{'experts':Expert.objects.all()})

@login_required(login_url='login_signup')
def cons_expert(request):
    if request.method == 'POST':
       name=request.POST['name']
       img=request.POST['img']
       Consults.objects.create(user=request.user,name=name,status='pending',exp_image=img)
       return render(request, 'expert_consultants.html',{'message':'Ok Your Request For Consult The Expert " '+ name + ' " is added ,We Will Notify You Once Expert Accept Your Request For Consult '})

@login_required(login_url='login_signup')
def conults(request):
    con=Consults.objects.filter(user=request.user)
    return render(request,'conults.html',{'consults':con})

@login_required(login_url='login_signup')
def cancel_slot(request,pk):
    id=Consults.objects.get(id=pk)
    print('expert id =',id)
    satus= id.status
    print('Status  is =',satus)

    print('slot name=',id.name )


    if id.status == 'Accepted':
        return render(request,'error.html',{'msg':'Sorry Ur Request Is Accepted By The Expert And Unable to Cancel The  Request..With In Shortly We Will Inform  Ur Slot Day And Time'})
    else:

       id.delete()
    return redirect('conults')



@login_required(login_url='login_signup')
def my_slots(request):

    return render(request,'my_slots.html')

@login_required(login_url='login_signup')
def book_slot(request,pk):
    id=Consults.objects.get(id=pk)
    name=id.name
    satus=id.status
    print('id=',id)
    if id.status=='Accepted':
        Slots.objects.create(name=name,status=satus,user=request.user)
        slots=Slots.objects.filter(user=request.user)
        Consults.objects.filter(id=pk).delete()
        return render(request,'my_slots.html',{'slots':slots})
    else:
        messge='Sorry Ur Request Is  not Accepted By The Expert  " '+ name +' " And Unable to Book Ur Slot At This Time ..With In Shortly We Will Inform  Ur Slot Day And Time Once The Expert Is Accepted Ur Request'
    return render(request,'error.html',{'message':messge})

