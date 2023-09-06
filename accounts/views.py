from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
import store.views


def signup(request):
    if request.method == "POST":
        if request.POST["password"] == request.POST["confirm_password"]:
            try:
                User.objects.get(username=request.POST["username"])
                return render (request, 'accounts/signup.html',{'error':'Email address already exists'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password'])
                auth.login(request, user)
                return redirect('home')
        else:
            return render(request, 'accounts/signup.html',{'error':'Passwords must match'})
    else:
        return render(request, 'accounts/signup.html')
def login(request):
    if request.method == "POST":
        user = auth.authenticate(username=request.POST["username"],password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request,'accounts/login.html',{'error':"Email and Password don't match"})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    auth.logout(request)
    return redirect('home')
