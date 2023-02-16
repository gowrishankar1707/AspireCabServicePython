from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def masterApp(request):
    template=loader.get_template('baseHtml.html')
    return HttpResponse(template.render())

def helpPage(request):
    helpString={'help':'This is help Page'}
    return render(request,'help.html',context=helpString)

# Create your views here.
