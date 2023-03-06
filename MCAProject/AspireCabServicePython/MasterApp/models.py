from django.db import models
from django.contrib.auth.models import User

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















