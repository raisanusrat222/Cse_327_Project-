from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def nav(request):
    diction= {}
    return render(request,'metro_app/nav.html',context=diction)
def login(request):
    diction= {}
    return render(request,'metro_app/login.html',context=diction)



   
