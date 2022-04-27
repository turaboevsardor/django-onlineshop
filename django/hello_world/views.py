from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse('Hello World')

def index2(request):
    return HttpResponse('About me')

def index3(request):
    return HttpResponse('Contacts')

def index(request):
    return render(request,'hello_world/index.html')


