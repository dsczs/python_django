from django.shortcuts import render

# Create your views here.


def hello(request):
    print("hello")
    return render(request,"hello.html")