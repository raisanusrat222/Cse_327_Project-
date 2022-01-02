from django.contrib import admin
from .models import SellTicket
from .models import Question
from .models import Answer

# Register SellTicket models here.
admin.site.register(SellTicket)
admin.site.register(Question)
admin.site.register(Answer)