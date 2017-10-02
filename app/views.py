from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import *
# Create your views here.


def hello(request):
    return render(request,"app/hello.html")


def say(request):
    return render(request, "say.html")


def user(request):
    user_list = User.objects.raw("select * from auth_user")
    for i in user_list:
        print(i.username)
        print(i.password)
    return render(request, "user.html", {"user_list": user_list})
