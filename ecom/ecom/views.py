from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages 
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def productView(request):
    return render(request, 'productView.html')

def loginUser(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            messages.success(request, ("Invalid Credentials, Please try again"))
            return redirect("/login")
    else:
        return render(request, 'login.html')
    
def logoutUser(request):
    logout(request)
    messages.success(request, ("You have been logged out"))
    return redirect("/login")
