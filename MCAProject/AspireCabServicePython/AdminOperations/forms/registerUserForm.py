from phonenumber_field.modelfields import PhoneNumberField
from django import forms
from MasterApp import models
from django.core import validators

class registerUser(forms.ModelForm):
    userEmailId=forms.EmailField(validators=[validators.MaxLengthValidator(30)],required=True)
    firstName=forms.CharField(validators=[validators.MaxLengthValidator(30)],required=True)
    lastName=forms.CharField(validators=[validators.MaxLengthValidator(30)],required=True)
    password=forms.CharField(validators=[validators.MaxLengthValidator(30)],required=True,widget=forms.PasswordInput)
    confirmPassword=forms.CharField(validators=[validators.MaxLengthValidator(30)],required=True,widget=forms.PasswordInput)
    DOB=forms.DateField(required=True,widget=forms.DateInput(format='%d/%m/%Y'))
    phoneNumber=PhoneNumberField(region='In')
    address=forms.Textarea()
    image=forms.ImageField(required=False)

    class Meta:
        model=models.User
        exclude = ('userRole','createdDate','updatedDate',)