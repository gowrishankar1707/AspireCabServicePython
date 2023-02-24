from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import UserRegistration

def masterApp(request):
    return render(request,'baseHtml.html')

def helpPage(request):
    helpString={'help':'This is help Page'}
    return render(request,'help.html',context=helpString)

# Create your views here.
