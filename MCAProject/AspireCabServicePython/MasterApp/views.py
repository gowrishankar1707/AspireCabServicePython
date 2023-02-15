from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

def masterApp(request):
    template=loader.get_template('baseHtml.html')
    return HttpResponse(template.render())

# Create your views here.
