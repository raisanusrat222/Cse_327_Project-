from django.contrib import admin
from metro_app.models import schedule_check
from metro_app.models import user_ticket
from metro_app.models import premium_ticket

# Register your models here.
admin.site.register(schedule_check),
admin.site.register(user_ticket),
admin.site.register(premium_ticket)