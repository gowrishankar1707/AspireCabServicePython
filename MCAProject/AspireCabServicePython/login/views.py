from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template import loader
from .Forms import login_form
from django.contrib.auth import login,authenticate,logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def login_view(request):

    

    if request.method == 'POST':
        userName=request.POST.get('username')
        password=request.POST.get('password')

        user=authenticate(username=userName,password=password)

        if user:
            if user.is_active:

                login(request,user)
                return HttpResponseRedirect(reverse("masterApp"))
            else:
                return HttpResponse("User is not activate")
        else:
            return render(request,"login.html",{'InCorrectCredentialls':"UserName or Password Is Incorrect"})
    return render(request,"login.html")

@login_required
def logout_view(request):
    logout(request)
    return render(request,'baseHtml.html',{"logoutStatus":"Logout Completed"})

# Create your views here.
