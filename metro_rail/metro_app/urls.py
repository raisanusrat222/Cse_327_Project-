from django.contrib import admin
from django.urls import path
from metro_app import views


urlpatterns = [
    path('',views.nav,name="nav"),
    path('pregister/', views.pregister,name="pregister"),
    path('PremiumPage/', views.PremiumPage,name="PremiumPage")

    

]
