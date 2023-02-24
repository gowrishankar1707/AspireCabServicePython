from phonenumber_field.modelfields import PhoneNumberField
from django import forms
from MasterApp import models
from django.core import validators

class registerUser(forms.ModelForm):
    image=forms.ImageField(required=False)
    class Meta:
        model=models.UserRegistration
        exclude=['userRole','updatedDate','user']


class userModelForm(forms.ModelForm):
    username=forms.CharField(max_length=30,validators=[validators.MaxLengthValidator(30)])
    password=forms.CharField(max_length=15,widget=forms.PasswordInput)
    email=forms.CharField(widget=forms.EmailInput)

    class Meta:
        model=models.User
        fields=['username','password','first_name','last_name','email']
