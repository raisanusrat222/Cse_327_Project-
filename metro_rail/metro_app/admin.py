from django.contrib import admin
from metro_app.models import schedule_check
from metro_app.models import user_ticket
from metro_app.models import PremiumMember
from metro_app.models import employee_ticket
from metro_app.models import Employee


# Register your models here.
admin.site.register(schedule_check),
admin.site.register(user_ticket),

admin.site.register(employee_ticket),


# Register your models here.

admin.site.register(PremiumMember)
admin.site.register(Employee)