from django.urls import path,re_path
from . import views

urlpatterns=[
    path('listRegisteredUser',views.listRegisteredUser.as_view(),name='listRegisteredUser'),
    path('registerUser',views.registerUsers,name='registerUser'),
    path('AddCab',views.AddCab.as_view(),name='addCabView'),
    path('CabList',views.ViewCabList.as_view() ,name='CabList'),
    re_path(r'^cabDetail/(?P<pk>\d+)/$',views.CabDetailedView.as_view(),name='cabDetail'),
    re_path(r'^cabUpdate/(?P<pk>\d+)/$',views.UpdateCabView.as_view(),name='cabUpdate'),
    re_path(r'^cabDelete/(?P<pk>\d+)/$',views.DeleteCabView.as_view(),name='cabDelete'),
    path('AddRoute',views.AddRoute.as_view() ,name='AddRoute'),
    re_path(r'^RouteDetail/(?P<pk>\d+)/$',views.RouteDetail.as_view(),name='RouteDetail'),
     path('RouteList',views.RouteList.as_view() ,name='RouteList'),
    

]