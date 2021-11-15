from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello, World!")

def brian(request):
    return HttpResponse("Hello, Brian!")

def david(request):
    return render(request, "hello/david.html")

def greetname(request, name):
    return render(request,"hello/greetname.html",{'name' : name.capitalize()})