from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import User

def masterApp(request):
    userList=User.objects.all()
    userdict={'user':userList}
    return render(request,'baseHtml.html',context=userdict)

def helpPage(request):
    helpString={'help':'This is help Page'}
    return render(request,'help.html',context=helpString)

# Create your views here.
