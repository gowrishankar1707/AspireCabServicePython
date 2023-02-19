from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .Forms import login_form
from MasterApp import models
def login(request):
    loginForm=login_form.loginForm()

    if request.method == 'POST':
        loginForm=login_form.loginForm(request.POST)
        if loginForm.is_valid():
            userName=loginForm.cleaned_data['userName']
            password=loginForm.cleaned_data['password']
            checkUserAvailability:bool=models.User.objects.all().filter(userEmailId=userName,password=password)
            if checkUserAvailability:
                print("User logged in ")
            else:
                print("***************************")



            return render(request,'login.html',{'form':loginForm})
    return render(request,'login.html',{'form':loginForm})
# Create your views here.
