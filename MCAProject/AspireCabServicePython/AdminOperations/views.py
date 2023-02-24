from django.shortcuts import render
from MasterApp import models
from .forms.registerUserForm import userModelForm,registerUser
from django.contrib.auth.decorators import login_required
from datetime import date


# Create your views here.

@login_required
def listRegisteredUser(request):
    listUsers=models.User.objects.all()
    dictUsers={'listUsers' : listUsers}
    return render(request,'listRegisteredUser.html',context=dictUsers)

@login_required
def registerUsers(request):
    registerUserObj=registerUser()
    UserModelObj=userModelForm()
    
    if request.method == 'POST':
        registerUserObj=registerUser(data=request.POST)
        UserModelObj=userModelForm(data=request.POST)
        if registerUserObj.is_valid() and UserModelObj.is_valid():
            try:
                userCommit=UserModelObj.save()
                userCommit.set_password(userCommit.password)
                userCommit.save()




                commitedObj= registerUserObj.save(commit=False)
                commitedObj.userRole='E'
                print(userCommit)
                commitedObj.user=userCommit

                commitedObj.updatedDate=date.today()
                commitedObj.save()
                print('registered successfully')
            except:
                raise Exception('Gowri')
        else:
            print('****************************')
    return render(request,'registerUser.html',{'registerUser':registerUserObj,'userObj':UserModelObj})
