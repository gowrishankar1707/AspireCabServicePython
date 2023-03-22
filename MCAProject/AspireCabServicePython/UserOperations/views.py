from django.shortcuts import render,redirect
from MasterApp import models
from django.contrib.auth.decorators import login_required
import sys

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
        print("**********************Hello world")
        print(f"{request.user.id}")
        print(route)
        print(cabDate)
        bookedRoute=models.Route.objects.filter(id=route)
        routeList=models.Route.objects.all()
        for route in routeList:
            bookedSeats.update({str(route):models.CabBooking.objects.filter(bookedDate=cabDate,route=route,isCancelled=False).count()})
        
        print(list(bookedRoute))
        return render(request,"bookCabHtml.html",context={"routeList":routeList,"cabDate":cabDate,"bookedSeats":bookedSeats})
    else:
        cabDate = ""
        bookedSeats={}
        routeList=""

    
    

    return render(request,"bookCabHtml.html")

@login_required
def getDay(request):
    return render(request,"getDay.html")


@login_required
def bookCabDetailPage(request):

    return render(request,"bookCabDetailPage.html")
