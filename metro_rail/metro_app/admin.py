from django.contrib import admin
from metro_app.models import Employee
from metro_app.models import PremiumMember

# Register your models here.

admin.site.register(PremiumMember)
admin.site.register(Employee)