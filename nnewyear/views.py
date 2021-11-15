from django.shortcuts import render
from datetime import datetime

# Create your views here.

def index(request):
    now=datetime.now()
    return render(request, 'nnewyear/index.html',{'newyear': now.day and now.month ==1})