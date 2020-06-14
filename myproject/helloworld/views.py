from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('hello world!')

def hello(request):
    return render(request, 'home.html', {'name':'tolun'})

def add(request):

    return render(request, 'result.html')



