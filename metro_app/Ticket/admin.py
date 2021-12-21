from django.contrib import admin
from .models import Trainfare
from .models import Complain
# Register your models here.
@admin.register(Trainfare)
class TrainFareAdmin(admin.ModelAdmin):
    list_display = ['trainid', 'trainname', 'trainsource', 'traindestination', 'trainarrival', 'trainreach', 'trainfare']
# Register your models here.
@admin.register(Complain)
class ComplainAdmin(admin.ModelAdmin):
    list_display = ['ComplainNo', 'Complainer', 'Contact', 'Complain']