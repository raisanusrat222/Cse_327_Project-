from django.contrib import admin
from .models import TrainFare
from .models import Complain
from .models import TicketSell


# Register your models here.
@admin.register(TrainFare)
class TrainFareAdmin(admin.ModelAdmin):
    list_display = ['trainid', 'trainname', 'trainsource', 'traindestination', 'trainarrival', 'trainreach',
                    'trainfare']


# Register your models here.
@admin.register(Complain)
class ComplainAdmin(admin.ModelAdmin):
    list_display = ['ComplainNo', 'Complainer', 'Contact', 'Complain']


@admin.register(TicketSell)
class TicketSellAdmin(admin.ModelAdmin):
    list_display = ['ticketNo', 'ticketSource', 'ticketDestination', 'date', 'noOfTicket', 'total', 'email']
