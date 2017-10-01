from django.shortcuts import render

# Create your views here.


def hello(request):
    return render(request,"hello.html")


def say(request):
    return render(request, "say.html")