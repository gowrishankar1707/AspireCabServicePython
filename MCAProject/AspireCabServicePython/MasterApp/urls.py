from django.urls import path
from .views import masterApp

urlpatterns=[
    path('',masterApp,name='masterApp')
]
