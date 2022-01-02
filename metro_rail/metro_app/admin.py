from django.contrib import admin
from metro_app.models import schedule_check
from metro_app.models import user_ticket
from metro_app.models import PremiumMember
from metro_app.models import employee_ticket
from metro_app.models import Employee

from django.contrib import admin
from .models import TrainFare
from .models import Complain
from .models import TicketSell


# Register your models here.
admin.site.register(schedule_check),
admin.site.register(user_ticket),

admin.site.register(employee_ticket),


# Register your models here.

admin.site.register(PremiumMember)
admin.site.register(Employee)






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
