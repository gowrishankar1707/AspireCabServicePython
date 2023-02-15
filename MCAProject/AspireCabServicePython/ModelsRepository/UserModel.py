from django.db import models

class User(models.Model):
    userId=models.BigIntegerField(primary_key=True)
    userName=models.CharField(max_length=35)
    password=models.CharField(max_length=15)
    DOB=models.DateField()
