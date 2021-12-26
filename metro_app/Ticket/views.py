from django.shortcuts import render
from django.core.mail import send_mail
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

    Ticket_info = TicketSell(ticketSource=src, ticketDestination=dst, date=date,noOfTicket=Nticket,email=email,total=total)
    Ticket_info.save()
    send_mail('Your Ticket is Ready!!', 'Your ticket for {} is confirmed.You have booked {} tickets.You can travel on {}.'.format(name,Nticket,date), 'dhaka.metroraill@gmail.com', [email], fail_silently=False)

    return render(request, 'Ticket/ShowTicketDetails.html', {"info":total,
                                                             "srcinfo":src,
                                                             "dstinfo":dst,
                                                             "emailinfo":email,
                                                             "noticket":Nticket,
                                                             "arrive":time,
                                                             "tname":name})
def CancelTickets(request):

    return render(request, 'Ticket/CancelTicket.html', {})


def AfterCancelTickets(request):
    canceldata = TicketSell.objects.all()
    ticketID = request.POST.get("ticket")
    date = request.POST.get("date")
    email = request.POST.get("email")
    name = canceldata.filter(ticketNo=ticketID, date=date, email=email)
    name.delete()
    send_mail('Your Ticket is Cancelled!!',
              'Your ticket scheduled on {} is Cancelled. - Dhaka Metro Rail'.format(date),
              'dhaka.metroraill@gmail.com', [email], fail_silently=False)

    return render(request, 'Ticket/CancelTicket.html', {})

def PostponeTickets(request):

    return render(request, 'Ticket/PostponeTicket.html', {})

def AfterPostponeTickets(request):
    postponedata = TicketSell.objects.all()
    ticketID = request.POST.get("ticket")
    odate = request.POST.get("odate")
    ndate = request.POST.get("ndate")
    email = request.POST.get("email")
    postponedata.filter(ticketNo=ticketID).update(date=ndate)


    send_mail('Your Ticket is Postponed!!',
              'Your ticket scheduled on {} is postponed to {}. - Dhaka Metro Rail'.format(odate,ndate),
              'dhaka.metroraill@gmail.com', [email], fail_silently=False)

    return render(request, 'Ticket/PostponeTicket.html', {})
def TicketMenu(request):

    return render(request, 'Ticket/TicketMenu.html', {})