from django.urls import path
from . import views

urlpatterns=[
    path('listRegisteredUser',views.listRegisteredUser,name='listRegisteredUser'),
    path('registerUser',views.registerUsers,name='registerUser')

]