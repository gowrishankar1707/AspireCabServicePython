from django.shortcuts import render
from MasterApp import models
from .forms import registerUserForm
from datetime import date


# Create your views here.


def listRegisteredUser(request):
    listUsers=models.User.objects.all()
    dictUsers={'listUsers' : listUsers}
    return render(request,'listRegisteredUser.html',context=dictUsers)


def registerUsers(request):
    registerUser=registerUserForm.registerUser()
    
    if request.method == 'POST':
        registerUser=registerUserForm.registerUser(request.POST)
        if registerUser.is_valid():
            try:

                commitedObj= registerUser.save(commit=False)
                commitedObj.createdDate=date.today()
                commitedObj.updatedDate=date.today()
                commitedObj.save()
                print('registered successfully')
            except:
                raise Exception()
        else:
            print('****************************')
    return render(request,'registerUser.html',{'registerUser':registerUser})
