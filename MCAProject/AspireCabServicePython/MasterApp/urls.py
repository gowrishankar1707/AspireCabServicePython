from django.urls import path,re_path
from .views import masterApp,helpPage

urlpatterns=[
    re_path(r'^masterApp/(?P<cabSeatingSuccessMessage>\w+)/$',masterApp,name='masterApp'),
    path('',masterApp,name='masterApp'),
    path('help',helpPage,name='help'),
    
]
