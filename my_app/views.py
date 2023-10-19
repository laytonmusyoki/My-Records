from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import login,logout,authenticate
from .forms import Registration
from .forms import Notesform
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .decorators import authenticated_users,allowed_users

# Create your views here.

@authenticated_users
def Register(request):
    user=Registration()
    if request.method=='POST':
        form=Registration(request.POST)
        if form.is_valid():
            user=form.save()
            group=Group.objects.get(name='other_users')
            user.groups.add(group)
            messages.info(request,f'Account created successfully')
            return redirect('login')
        else:
            context={
                'forms':user
            }
            return render(request,'register.html',context)
    context={
        'forms':user
    }
    return render(request,'register.html',context)


@authenticated_users
def signin(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            messages.success(request,f'Continue from where you left {username}')
            if request.user.groups.filter(name='admin').exists():
                return redirect('usermanager')
            return redirect('home')
        else:
            messages.warning(request,'You have entered wrong credentials')
            context={'username':username,
                    'password':password}
            return render(request,'login.html',context)
            return redirect('login')
    return render(request,'login.html')


@login_required(login_url='login')
def home(request):
    forms=Notesform()
    if request.method=='POST':
        form=Notesform(request.POST)
        if form.is_valid():
            data=form.save(commit=False)
            data.user=request.user
            data.save()
            messages.success(request,"Notes added successfully")
    context={
        'form':forms
    }
    return render(request,'home.html',context)


@allowed_users(user_roles=['admin'])
def usermanager(request):
    return render(request,'managers.html')


def Logout(request):
    logout(request)
    messages.warning(request,"You have been logged out")
    return redirect('login')