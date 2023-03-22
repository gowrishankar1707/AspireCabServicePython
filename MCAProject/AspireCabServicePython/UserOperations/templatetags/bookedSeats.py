from django import template
from django.template.defaultfilters import stringfilter
from MasterApp import models

register=template.Library()

@register.filter(name='bookedSeatNo')
def bookedSeatNo(dictionary,key):
    route=models.Route.objects.filter(routeName=key).values_list()
    route=list(route)
    noOfActualSeats=int(route[0][2])
    noOfSeatsBooked=int(dictionary[key])
    return noOfActualSeats-noOfSeatsBooked
    