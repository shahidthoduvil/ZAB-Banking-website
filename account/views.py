from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from home.views import home 
from django.contrib.auth.models import Group
from .decorators import *
# Create your views here.



@unauthenticated_user
def registerPage(request):
    form=CreateUserForm()
    if request.method=='POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
             user=form.save()
             group=Group.objects.get(name='customer')
             user.groups.add(group)
             messages.success(request,'Account was created')
             return  redirect('login')
        
    context={'form':form}
    return render(request,'accounts/register.html',context)

@unauthenticated_user
def loginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('newpage')
        else:
            messages.info(request,'Username or Password is incorrect ')
    context={}
    return render(request,'accounts/login.html',context)

def logoutuser(request):
    logout(request)
    return redirect('login')


