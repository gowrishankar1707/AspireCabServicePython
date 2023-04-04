from django.shortcuts import render,redirect
from MasterApp import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
import sys
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.views.generic import DetailView,UpdateView
from django.utils.decorators import *

# Create your views here.
@login_required
def bookCab(request,route,cabDate):
    bookedSeats={}
    routeList=""

    if request.method == 'GET':
        

        try:
            cabDate=request.GET.get('cabDate')

            if not cabDate == None:
                
                routeList=models.Route.objects.all()
                for route in routeList:
                    bookedSeats.update({str(route):models.CabBooking.objects.filter(bookedDate=cabDate,route=route,isCancelled=False).count()})
                return render(request,"bookCabHtml.html",context={"routeList":routeList,"cabDate":cabDate,"bookedSeats":bookedSeats})
                    
            
            
        except Exception as e:
            exception_type, exception_object, exception_traceback = sys.exc_info()
            filename = exception_traceback.tb_frame.f_code.co_filename
            line_number = exception_traceback.tb_lineno

            print(f"{type(e).__name__} was raised: {e}")
            print(line_number)
    elif request.method == "POST":
        bookedCabSeatsCount=bookedSeatCount(routeId=route,cabBookedDate=cabDate)
        if bookedCabSeatsCount >0:
            try:
                """ cabBookingSuccessFunc(request=request,route=route,cabDate=cabDate,bookedCabSeatsCount=bookedCabSeatsCount)"""

        
                """bookedRoute=models.Route.objects.get(id=route)
                bookedShift=list(models.Route.objects.filter(id=route).values_list('shift'))[0][0]
                cabBookObj=models.CabBooking(userRe=User.objects.get(id=request.user.id),route=bookedRoute,shift=bookedShift,bookedDate=cabDate)
                cabBookObj.save()
                cabSeatingSuccessMessage=getRouteNameById(routeId=route,cabBookedDate=cabDate,bookedCabSeatsCount=bookedCabSeatsCount)"""
                return  HttpResponseRedirect(reverse('cabBookingSuccessFunc',kwargs={"route":route,"cabDate":cabDate,"bookedCabSeatsCount":bookedCabSeatsCount}))
                """return render(request,"cabBookingSuccess.html",content_type={"cabSeatingSuccessMessage":cabSeatingSuccessMessage})"""
            except Exception as e:
                 exception_type, exception_object, exception_traceback = sys.exc_info()
                 filename = exception_traceback.tb_frame.f_code.co_filename
                 line_number = exception_traceback.tb_lineno

                 print(f"{type(e).__name__} was raised: {e}")
                 print(line_number)

        else:
            bookSeatsErrorMsg=getRouteNameById(routeId=route,cabBookedDate=cabDate,bookedCabSeatsCount=bookedCabSeatsCount)

            routeList=models.Route.objects.all()
            for route in routeList:
                bookedSeats.update({str(route):models.CabBooking.objects.filter(bookedDate=cabDate,route=route,isCancelled=False).count()})
            
            return render(request,"bookCabHtml.html",context={"routeList":routeList,"cabDate":cabDate,"bookedSeats":bookedSeats,"bookSeatsErrorMsg":bookSeatsErrorMsg})
    else:
        cabDate = ""
        bookedSeats={}
        routeList=""

    
    

    return render(request,"bookCabHtml.html")

@login_required
def cabBookingSuccessFunc(request,**kwargs):
    for item,val in kwargs.items():
        print(f"{item} {val}")
    route=kwargs["route"]
    cabDate=kwargs["cabDate"]
    bookedCabSeatsCount=int(kwargs["bookedCabSeatsCount"])
    print("**************hellow")
    bookedRoute=models.Route.objects.get(id=route)
    bookedShift=list(models.Route.objects.filter(id=route).values_list('shift'))[0][0]
    cabBookObj=models.CabBooking(userRe=User.objects.get(id=request.user.id),route=bookedRoute,shift=bookedShift,bookedDate=cabDate)
    cabBookObj.save()
    cabSeatingSuccessMessage=getRouteNameById(routeId=route,cabBookedDate=cabDate,bookedCabSeatsCount=bookedCabSeatsCount)
    """return HttpResponseRedirect(reverse("cabBookingSuccessFunc",kwargs={"cabSeatingSuccessMessage":cabSeatingSuccessMessage}))"""
    return render(request,"cabBookingSuccess.html",context={"cabSeatingSuccessMessage":cabSeatingSuccessMessage})

@login_required
def getDay(request):
    return render(request,"getDay.html")




@login_required
def bookCabDetailPage(request):

    return render(request,"bookCabDetailPage.html")

def bookedSeatCount(routeId,cabBookedDate):
    try:
        routeTableObj=models.Route.objects.get(id=routeId)
        cabBookingTableCount=models.CabBooking.objects.filter(route=routeTableObj,bookedDate=cabBookedDate).count()
        routeTableObj=models.Route.objects.filter(id=routeId).values_list('cab')
        cabId=(list(routeTableObj))[0][0]
        noOfActualSeats=int((list(models.Cab.objects.filter(id=cabId).values_list('noOfSeats')))[0][0])
        return noOfActualSeats-cabBookingTableCount
    except Exception as e:
                 exception_type, exception_object, exception_traceback = sys.exc_info()
                 filename = exception_traceback.tb_frame.f_code.co_filename
                 line_number = exception_traceback.tb_lineno

                 print(f"{type(e).__name__} was raised: {e}")
                 print(line_number)
                 return 0
    
def getRouteNameById(routeId,cabBookedDate,bookedCabSeatsCount):
     try:
        if bookedCabSeatsCount > 0:
            routeTableObj=models.Route.objects.filter(id=routeId).values_list('routeName')
            routeName=list(routeTableObj)[0][0]
            successMsg=f"Your {routeName} cab booked on this date: {cabBookedDate} "
            return successMsg
        else:
             routeTableObj=models.Route.objects.filter(id=routeId).values_list('routeName')
             routeName=list(routeTableObj)[0][0]
             errorMessage=f"Your {routeName} cab cannot able to book on this date: {cabBookedDate} Because There is no available seats "
             return errorMessage
     except Exception as e:
                 exception_type, exception_object, exception_traceback = sys.exc_info()
                 filename = exception_traceback.tb_frame.f_code.co_filename
                 line_number = exception_traceback.tb_lineno

                 print(f"{type(e).__name__} was raised: {e}")
                 print(line_number)
                 return None
     

@login_required
def userDetailedViewByUser(request,**kwargs):
     userReObject=""
     userReDict=""
     id=kwargs['pk']
     userObject=models.User.objects.get(id=id)
     userObjList=list(list(models.User.objects.filter(id=id).values_list('username','first_name','last_name','email'))[0])
     userDict={"username":userObjList[0],"first_name":userObjList[1],"last_name":userObjList[2],"email":userObjList[3]}

     try:
        userReObject=list(list(models.UserRegistration.objects.filter(user=userObject).values_list('id','DOB','phoneNumber','address','image'))[0])
        
     except Exception as e:
        userReObject=""

     try:
      userReDict={"id":userReObject[0],
                  "DOB":userReObject[1],
                  "phoneNumber":userReObject[2],
                  "address":userReObject[3],
                  "image":userReObject[4]}
     except:
          userReDict=""
        

     return render(request,"userDetailedViewHtml.html",context={"userDetailedViewByUserObject":userDict,"userReObject":userReDict})

@login_required
def updateUserDetailFunc(request,**kwargs):
     print("Hellow world")
     userReObject=""
     userReDict=""
     id=kwargs['pk']
     userObject=models.User.objects.get(id=id)
     userObjList=list(list(models.User.objects.filter(id=id).values_list('username','first_name','last_name','email'))[0])
     userDict={"username":userObjList[0],"first_name":userObjList[1],"last_name":userObjList[2],"email":userObjList[3]}

     try:
        userReObject=list(list(models.UserRegistration.objects.filter(user=userObject).values_list('id','DOB','phoneNumber','address','image'))[0])
        
     except Exception as e:
        userReObject=""

     try:
      userReDict={"id":userReObject[0],
                  "DOB":userReObject[1],
                  "phoneNumber":userReObject[2],
                  "address":userReObject[3],
                  "image":userReObject[4]}
     except:
          userReDict=""
     return render(request,"",context={"asdf":""})
     
