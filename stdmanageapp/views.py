from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.

def home(request):
    return render(request,"index.html")

def signUp(request):
    if request.method=="POST":
        first_name=request.POST.get("first_name")
        last_name=request.POST.get("last_name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        con_password=request.POST.get("con_password")
        if password==con_password:
            if User.objects.filter(username=email).exists():
                messages.error(request,"Email already exists")
            else:
                User.objects.create_user(username=email,
                                         email=email,
                                         first_name=first_name,
                                         last_name=last_name)
                messages.success(request,"New user created . Please login to continue")
                return redirect("login")
        else:
            messages.error(request,"Both passwords must be same")
            return redirect("register")
    return render(request,"register.html")

def signIn(request):
    return render(request,"login.html")