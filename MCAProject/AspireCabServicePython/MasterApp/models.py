from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserRole(models.Model):
    
    userRole=models.CharField(max_length=1,unique=True,default='E')
    def __str__(self) -> str:
        return self.userRole
    
class UserRegistration(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    DOB=models.DateField(null=False,max_length=10)
    updatedDate=models.DateField(null=False,max_length=10)
    phoneNumber=models.CharField(max_length=10,unique=True,null=False)
    address=models.CharField(max_length=254,null=True)
    image=models.ImageField(null=True,upload_to='userProfilePicture')
    userRole=models.ForeignKey(UserRole,on_delete=models.DO_NOTHING,to_field='userRole',default='E')

    def __str__(self):
        return self.user.username;









