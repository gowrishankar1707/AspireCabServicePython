from django.db import models

# Create your models here.


class User(models.Model):
    userEmailId=models.CharField(primary_key=True,max_length=30)
    firstName=models.CharField(max_length=30,null=False)
    lastName=models.CharField(max_length=30,null=False)
    password=models.CharField(max_length=30,null=False)
    DOB=models.DateField(null=False,max_length=10)
    createdDate=models.DateField(null=False,max_length=10)
    updatedDate=models.DateField(null=False,max_length=10)
    phoneNumber=models.CharField(max_length=10,unique=True,null=False)
    address=models.CharField(max_length=254,null=True)
    image=models.ImageField(null=True)





