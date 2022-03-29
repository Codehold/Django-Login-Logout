from django.shortcuts import render,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from .models import *



def user_login(request):
    if not request.user.is_authenticated: 
        if request.method == "POST":
            fm = AuthenticationForm(request=request,data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'welcome')
                    return HttpResponseRedirect('/profile/')
        else:            
            fm=AuthenticationForm()
        return render(request, 'registration/login.html',{'form':fm})
    else:
        return HttpResponseRedirect('/profile/')

def user_profile(request):
    if request.user.is_authenticated:
        userdata = Profile.objects.filter(author=request.user)
        userinstall = Installament.objects.filter(user=request.user.salman)

        return render(request,'registration/profile.html',{'profiles':userdata,'installments':userinstall})
    else:
        return HttpResponseRedirect('/login/')    

def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')