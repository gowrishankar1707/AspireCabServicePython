from django.urls import path,re_path
from . import views


urlpatterns=[
    path("bookCab",views.bookCab,name="bookCab"),
    re_path(r"^bookCabPOST/(?P<route>\d+)/(?P<cabDate>\d{4}-\d{2}-\d{2})/$",views.bookCab,name="bookCabPOST"),
    re_path(r"^bookCab?(?P<cabDate>\w+)&(?P<csrfmiddlewaretoken>\w+)$",views.bookCab,name="bookCab"),
    re_path(r"^bookCab/(?P<route>\w+)/(?P<cabDate>\w+)/$",views.bookCab,name="bookCab"),
    re_path(r"^cabBookingSuccessFunc/(?P<route>\w+)/(?P<cabDate>\d{4}-\d{2}-\d{2})/(?P<bookedCabSeatsCount>\w+)/$",views.cabBookingSuccessFunc,name="cabBookingSuccessFunc"),
    re_path(r"^userDetailedViewByUser/(?P<pk>\w+)/$",views.userDetailedViewByUser,name="userDetailedViewByUser"),
    re_path(r"^updateUserDetailFunc/(?P<userObj>\w+)/$",views.updateUserDetailFunc,name="updateUserDetailFunc"),
    
    
    
    
]