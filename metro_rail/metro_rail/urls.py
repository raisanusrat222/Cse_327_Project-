
"""MetroRail URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from Ticket import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Ticket.urls')),
    # path('Fare/', views.fare),
    # path('Complains/', views.complains,name="Complains"),
    # path('AfterComplain/', views.aftercomplain, name="AfterComplain"),
    # path('SeeComplains/', views.seecomplains, name="SeeComplains"),
    # path('BuyTickets/', views.buytickets,name="BuyTickets"),
    # path('AfterTickets/', views.aftertickets, name="AfterTickets"),
    # path('CancelTickets/', views.canceltickets,name="CancelTickets"),
    # path('AfterCancelTickets/', views.aftercanceltickets, name="AfterCancelTickets"),
    # path('PostponeTickets/', views.postponetickets,name="PostponeTickets"),
    # path('AfterPostponeTickets/', views.afterpostponetickets, name="AfterPostponeTickets"),
    # path('TicketMenu/', views.ticketmenu,name="TicketMenu"),
    # path('GenTicket/', views.genticket, name="GenTicket"),

]
# =======
#
# from django.contrib import admin
# from django.urls import path,include
# from metro_app import views
#
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('',views.nav,name="nav"),
#     path('',include('metro_app.urls')),
#
#
# ]
#
# >>>>>>> main
