from django import template
from django.template.defaultfilters import stringfilter
from MasterApp import models

register=template.Library()

@register.filter(name='bookedSeatNo')
def bookedSeatNo(dictionary,key):
    route=models.Route.objects.filter(routeName=key).values_list('cab')
    cabId=(list(route))[0][0]
    noOfActualSeats=int((list(models.Cab.objects.filter(id=cabId).values_list('noOfSeats')))[0][0])

    print(f"****************************{noOfActualSeats}")
    """noOfActualSeats=int(route[0][2])"""
    noOfSeatsBooked=int(dictionary[key])
    return noOfActualSeats-noOfSeatsBooked
    