from django.shortcuts import render
from .models import Trainfare
from .models import Complain
from .models import TicketSell
import math
# Create your views here.
def Ticket(request):
    traindata = Trainfare.objects.all()
    return render(request, 'Ticket/Ticket.html', {'traininfo':traindata})
def Fare(request):
    faredata = Trainfare.objects.all()
    source = request.GET.get('search1')
    destination = request.GET.get('search2')
    if source != '' and source is not None:
        faredata = faredata.filter(trainsource__icontains=source)
        if destination != '' and destination is not None:
            faredata = faredata.filter(traindestination=destination)
    context ={
        'queryset': faredata
    }
    return render(request, 'Ticket/Fare.html', context)

def Complains(request):

    return render(request, 'Ticket/Complain.html', {})

def AfterComplain(request):
    comp = request.POST.get("fname")
    contact = request.POST.get("contact")
    complain = request.POST.get("subject")
    complain_info = Complain(Complainer=comp, Contact=contact, Complain=complain)
    complain_info.save()
    return render(request, 'Ticket/Complain.html', {"message": "Registered!"})

def SeeComplains(request):
    comdata = Complain.objects.all()
    return render(request, 'Ticket/SeeComplain.html', {'cominfo':comdata})

def BuyTickets(request):

    return render(request, 'Ticket/BuyTicket.html', {})


def AfterTickets(request):
    tiketdata = Trainfare.objects.all()
    src = request.POST.get("source")
    dst = request.POST.get("destination")
    email = request.POST.get("email")
    date = request.POST.get("date")
    Nticket = request.POST.get("ticket")
    name = tiketdata.filter(trainsource=src).values_list('trainname', flat=True).first()
    time=tiketdata.filter(trainsource=src).values_list('trainarrival', flat=True).first()
    total=tiketdata.filter(trainsource=src).values_list('trainfare', flat=True).first()
    N=total*2
    Ticket_info = TicketSell(ticketSource=src, ticketDestination=dst, date=date,noOfTicket=Nticket,email=email,total=N)
    Ticket_info.save()

    return render(request, 'Ticket/ShowTicketDetails.html', {"info":N,
                                                             "srcinfo":src,
                                                             "dstinfo":dst,
                                                             "emailinfo":email,
                                                             "noticket":Nticket,
                                                             "arrive":time,
                                                             "tname":name})

