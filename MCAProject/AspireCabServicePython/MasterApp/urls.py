from django.urls import path
from .views import masterApp,helpPage

urlpatterns=[
    path('',masterApp,name='masterApp'),
    path('help',helpPage,name='help'),
]
