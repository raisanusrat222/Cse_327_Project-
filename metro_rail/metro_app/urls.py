from django.contrib import admin
from django.urls import path
from metro_app import views


urlpatterns = [
    path('',views.nav,name="nav"),
    path('login/',views.loginPage,name="login"),
    path('logout/', views.logoutUser, name="logout"),
    
    path('scheck/',views.schedule_checks,name="scheck"),
    path('adpage/',views.admin_pages,name="adpage"),
    path('usticket/',views.user_tickets,name="usticket"),
    path('empticket/',views.employee_tickets,name="empticket"),
    path('preticket/',views.premium_tickets,name="preticket"),
    

    path('pregister/', views.pregister,name="pregister"),
    path('PremiumPage/', views.premiumpage,name="PremiumPage"),
    path('empregister/',views.empregister, name="empregister"),
    path('TicketValid/',views.TicketValid, name="TicketValid"),
    path('employeepage/', views.employeepage, name='employeepage'),


    
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
