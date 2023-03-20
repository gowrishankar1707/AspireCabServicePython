from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


    
class UserRegistration(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    DOB=models.DateField(null=False,max_length=10)
    updatedDate=models.DateField(null=False,max_length=10)
    phoneNumber=models.CharField(max_length=10,unique=True,null=False)
    address=models.CharField(max_length=254,null=True)
    image=models.ImageField(null=True,upload_to='userProfilePicture')

    def __str__(self):
        return self.user.username;


class Cab(models.Model):
    cabName=models.CharField(max_length=30)
    noOfSeats=models.IntegerField()

    def __str__(self):
        return self.cabName
    
    def get_absolute_url(self):
        return reverse("cabDetail",args=[str(self.id)])
    


class Route(models.Model):
    routeName=models.CharField(max_length=30,blank=True)
    cab=models.ForeignKey(Cab,on_delete=models.CASCADE,blank=True)
    shift=models.CharField(max_length=10,blank=True)
    timingDescription=models.CharField(max_length=30,blank=True)
    routeDescription=models.CharField(max_length=250,blank=True)

    def __str__(self):
        return self.routeName
    
    def get_absolute_url(self):
        return reverse("RouteDetail",args=[str(self.id)])
    

class CabBooking(models.Model):
    userRe=models.ForeignKey(UserRegistration,on_delete=models.CASCADE,blank=True)
    route=models.ForeignKey(Route,on_delete=models.CASCADE)
    shift=models.CharField(max_length=10,blank=True)
    isCancelled=models.BooleanField(blank=True,default=False)
    bookedDate=models.DateField(blank=True)

    def __str__(self) -> str:
        return self.userRe.user.username+"_"+self.bookedDate+"_"+self.shift















