from django.shortcuts import render
from MasterApp import models
from .forms import registerUserForm


# Create your views here.


def listRegisteredUser(request):
    listUsers=models.User.objects.all()
    dictUsers={'listUsers' : listUsers}
    return render(request,'listRegisteredUser.html',context=dictUsers)


def registerUsers(request):
    registerUser=registerUserForm.registerUser()
    
    if request.method == 'POST':
        print('hello')
        registerUser=registerUserForm.registerUser(request.POST)
        print('hello')
        if registerUser.is_valid():
            print('registered successfully')
        else:
            print('****************************')
    return render(request,'registerUser.html',{'registerUser':registerUser})
