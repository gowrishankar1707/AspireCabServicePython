from django import forms
from django.core import validators

class loginForm(forms.Form):
    userName = forms.CharField(validators=[validators.MaxLengthValidator(30)],widget=forms.EmailInput(),required=True)
    password=forms.CharField(validators=[validators.MaxLengthValidator(30)],widget=forms.PasswordInput(),required=True)