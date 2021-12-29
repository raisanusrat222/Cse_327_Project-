from django.contrib import admin
from metro_app.models import Employee
from metro_app.models import Premium_Member

# Register your models here.

admin.site.register(Premium_Member)
admin.site.register(Employee)