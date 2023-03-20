from django.shortcuts import render
from MasterApp import models
from .forms.registerUserForm import userModelForm,registerUser
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import *
from datetime import date
from django.http import HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django.views.generic import *

commonDecorators=[login_required,staff_member_required]

# Create your views here.


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


@method_decorator(commonDecorators,name='dispatch')
class AddCab(CreateView):
    fields=['cabName','noOfSeats']
    model=models.Cab
    template_name='addCab.html'


@method_decorator(commonDecorators,name='dispatch')
class ViewCabList(ListView):
    context_object_name='cabLists'
    model=models.Cab
    template_name='cabList.html'
   
    

@method_decorator(commonDecorators,name='dispatch')
class CabDetailedView(DetailView):
    context_object_name='cabDetailObject'
    model=models.Cab
    template_name='cabDetail.html'


@method_decorator(commonDecorators,name='dispatch')
class UpdateCabView(UpdateView):
    model=models.Cab
    fields=['cabName','noOfSeats']
    context_object_name='updateCabObj'
    template_name='updateCabHtml.html'


@method_decorator(commonDecorators,name='dispatch')
class DeleteCabView(DeleteView):
    model=models.Cab
    template_name='cabDeleteHtml.html'
    success_url = reverse_lazy('CabList')




@method_decorator(commonDecorators,name='dispatch')
class listRegisteredUser(ListView):

    
    model=models.UserRegistration
    queryset = models.UserRegistration.objects.order_by('-user')
    context_object_name='usersList'
    template_name='listRegisteredUser.html'

"""
Route Table Crud Operations
"""
@method_decorator(commonDecorators,name='dispatch')
class AddRoute(CreateView):
    model=models.Route
    fields=['routeName','cab','shift','timingDescription','routeDescription']
    template_name='addRouteHtml.html'

@method_decorator(commonDecorators,name='dispatch')
class RouteDetail(DetailView):
    model=models.Route
    context_object_name='routeDetailObj'
    template_name='routeDetailHtml.html'

@method_decorator(commonDecorators,name='dispatch')
class RouteList(ListView):
    model=models.Route
    context_object_name='routeListObj'
    template_name='routeListHtml.html'








