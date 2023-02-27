from django.shortcuts import render
from MasterApp import models
from .forms.registerUserForm import userModelForm,registerUser
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from datetime import date
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.

@login_required
@staff_member_required
def listRegisteredUser(request):
    listUsers=models.User.objects.all()
    dictUsers={'listUsers' : listUsers}
    return render(request,'listRegisteredUser.html',context=dictUsers)

@login_required
@staff_member_required
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
                




                commitedObj= registerUserObj.save(commit=False)
                commitedObj.user=userCommit
                commitedObj.updatedDate=date.today()
                if 'userProfilePicture' in request.FILES:
                    commitedObj.image=request.FILES['userProfilePicture']

                
                userCommit.save()
                commitedObj.save()
                return render(request,'registerUser.Html',{'registerMessage':'Registered '})
            except:
                raise Exception('Gowri')
        else:
            print('****************************')
    return render(request,'registerUser.html',{'registerUser':registerUserObj,'userObj':UserModelObj})

@login_required
@staff_member_required
def addCabView(request):
    return render(request,'addCab.html')

