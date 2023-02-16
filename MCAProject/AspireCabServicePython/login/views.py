from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
def login(request):
    sampleDict={'hello':"Hi Im Gowrishankar"}
    return render(request,'login.html',context=sampleDict)
# Create your views here.
