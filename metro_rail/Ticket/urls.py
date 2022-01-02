from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ticket),
    path('Fare/', views.fare),
    path('Complains/', views.complains,name="Complains"),
    path('AfterComplain/', views.aftercomplain, name="AfterComplain"),
    path('SeeComplains/', views.seecomplains, name="SeeComplains"),
    path('BuyTickets/', views.buytickets,name="BuyTickets"),
    path('AfterTickets/', views.aftertickets, name="AfterTickets"),
    path('CancelTickets/', views.canceltickets,name="CancelTickets"),
    path('AfterCancelTickets/', views.aftercanceltickets, name="AfterCancelTickets"),
    path('PostponeTickets/', views.postponetickets,name="PostponeTickets"),
    path('AfterPostponeTickets/', views.afterpostponetickets, name="AfterPostponeTickets"),
    path('TicketMenu/', views.ticketmenu,name="TicketMenu"),
    path('GenTicket/', views.genticket, name="GenTicket"),

]
