from django.contrib import admin
from django.urls import path
from metro_app import views


urlpatterns = [
    path('',views.nav,name="nav"),
    path('pregister/', views.pregister,name="pregister"),
    path('PremiumPage/', views.premiumpage,name="PremiumPage"),
    path('empregister/',views.empregister, name="empregister"),
    path('TicketValid/',views.TicketValid, name="TicketValid")

    

]
