from django.shortcuts import render
from django.core.mail import send_mail
from .models import TrainFare
from .models import Complain
from .models import TicketSell
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter


def ticket(request):
    """
        This method is used to view the Home.

        :param request: it's a HttpResponse from user.

        :type request: HttpResponse.

        :return: this method returns a Home Page which is a HTML page.

        :rtype: HttpResponse.

    """
    train_data = TrainFare.objects.all()
    return render(request, 'Ticket/Ticket.html', {'traininfo':train_data})
def fare(request):
    """
        This method is used to view the Fare Chart page.If we search using a Source and Destination

        it will return the Fare for that specific route.

        :param request: it's a HttpResponse from user.

        :type request: HttpResponse.

        :return: this method returns a Fare page which is a HTML page.

        :rtype: HttpResponse.


    """
    fare_data = TrainFare.objects.all()
    source = request.GET.get('search1')
    destination = request.GET.get('search2')
    if source != '' and source is not None:
        fare_data = fare_data.filter(trainsource__icontains=source)
        if destination != '' and destination is not None:
            fare_data = fare_data.filter(traindestination=destination)
    context ={
        'queryset': fare_data
    }
    return render(request, 'Ticket/Fare.html', context)

def complains(request):
    """
        This method is used to view the Complain Form page.User submit their complain in the Form.

        :param request: it's a HttpResponse from user.

        :type request: HttpResponse.

        :return: this method returns a Complain Page which is a HTML page.

        :rtype: HttpResponse.

    """

    return render(request, 'Ticket/Complain.html', {})

def aftercomplain(request):
    """
        This method is used to Submit the Complain page in Database.

        :param request: it's a HttpResponse from user.

        :type request: HttpResponse.

        :return: this method returns to a blank Complain Page again which is a HTML page and delivers a message.

        :rtype: HttpResponse.

    """
    comp = request.POST.get("fname")
    contact = request.POST.get("contact")
    complain = request.POST.get("subject")
    complain_info = Complain(Complainer=comp, Contact=contact, Complain=complain)
    complain_info.save()
    return render(request, 'Ticket/Complain.html', {"message": "Registered!"})

def seecomplains(request):
    """
        This method is used to view complain the login page to the Adminstrator. Administrator can see all submitted complains here.

        :param request: it's a HttpResponse from user.

        :type request: HttpResponse.

        :return: this method returns a SeeComplain Page which is a HTML page.

        :rtype: HttpResponse.

    """
    com_data = Complain.objects.all()
    return render(request, 'Ticket/SeeComplain.html', {'cominfo':com_data})

def buytickets(request):
    """
        This method is used to view the BuyTicket page.User buys ticket online using this page.

        :param request: it's a HttpResponse from user.

        :type request: HttpResponse.

        :return: this method returns a BuyTicket page which is a HTML page.

        :rtype: HttpResponse.

    """

    return render(request, 'Ticket/BuyTicket.html', {})

def aftertickets(request):
    """
        This method is used to Save details required to buy ticket in Database and send a confirmation email to user.

        :param request: it's a HttpResponse from user.

        :type request: HttpResponse.

        :return: this method returns a ShowTicketDetails page which is a HTML page and Sends an Email.

        :rtype: HttpResponse.

    """
    ticket_data = TrainFare.objects.all()
    src = request.POST.get("source")
    dst = request.POST.get("destination")
    email = request.POST.get("email")
    date = request.POST.get("date")
    nticket = request.POST.get("ticket")
    name = ticket_data.filter(trainsource=src).values_list('trainname', flat=True).first()
    time=ticket_data.filter(trainsource=src).values_list('trainarrival', flat=True).first()
    total=ticket_data.filter(trainsource=src).values_list('trainfare', flat=True).first()

    Ticket_info = TicketSell(ticketSource=src, ticketDestination=dst, date=date,noOfTicket=nticket,email=email,total=total)
    Ticket_info.save()
    send_mail('Your Ticket is Ready!!', 'Your ticket for {} is confirmed.You have booked {} tickets.You can travel on {}.'.format(name,nticket,date), 'dhaka.metroraill@gmail.com', [email], fail_silently=False)

    return render(request, 'Ticket/ShowTicketDetails.html', {"info":total,
                                                             "srcinfo":src,
                                                             "dstinfo":dst,
                                                             "emailinfo":email,
                                                             "noticket":nticket,
                                                             "arrive":time,
                                                             "tname":name})
def canceltickets(request):
    """
            This method is used to view the Cancel ticket Form. User put their ticket Id to cancel their ticket.

            :param request: it's a HttpResponse from user.

            :type request: HttpResponse.

            :return: this method returns a CancelTicket Page which is a HTML page.

            :rtype: HttpResponse.

    """

    return render(request, 'Ticket/CancelTicket.html', {})


def aftercanceltickets(request):
    """
            This method is used to Cancel the ticket and Send a email.

            :param request: it's a HttpResponse from user.

            :type request: HttpResponse.

            :return: this method returns a CancelTicket Page which is a HTML page and Sends an email.

            :rtype: HttpResponse.

    """
    cancel_data = TicketSell.objects.all()
    ticket_id = request.POST.get("ticket")
    date = request.POST.get("date")
    email = request.POST.get("email")
    name = cancel_data.filter(ticketNo=ticket_id, date=date, email=email)
    name.delete()
    send_mail('Your Ticket is Cancelled!!',
              'Your ticket scheduled on {} is Cancelled. - Dhaka Metro Rail'.format(date),
              'dhaka.metroraill@gmail.com', [email], fail_silently=False)

    return render(request, 'Ticket/CancelTicket.html', {})

def postponetickets(request):
    """
            This method is used to view the Postpone ticket Form. User puts their ticketId and Dates to postpone their trip.

            :param request: it's a HttpResponse from user.

            :type request: HttpResponse.

            :return: this method returns a PostponeTicket Page which is a HTML page.

            :rtype: HttpResponse.

    """

    return render(request, 'Ticket/PostponeTicket.html', {})

def afterpostponetickets(request):
    """
            This method is used to Postpone trip of user and update Database.Also sends a confirmation email.

            :param request: it's a HttpResponse from user.

            :type request: HttpResponse.

            :return: this method returns a PostponeTicket Page which is a HTML page and Sends an Email.

            :rtype: HttpResponse.

    """
    postpone_data = TicketSell.objects.all()
    ticket_id = request.POST.get("ticket")
    odate = request.POST.get("odate")
    ndate = request.POST.get("ndate")
    email = request.POST.get("email")
    postpone_data.filter(ticketNo=ticket_id).update(date=ndate)


    send_mail('Your Ticket is Postponed!!',
              'Your ticket scheduled on {} is postponed to {}. - Dhaka Metro Rail'.format(odate,ndate),
              'dhaka.metroraill@gmail.com', [email], fail_silently=False)

    return render(request, 'Ticket/PostponeTicket.html', {})
def ticketmenu(request):
    """
            This method is used to view the TicketMenu.

            :param request: it's a HttpResponse from user.

            :type request: HttpResponse.

            :return: this method returns a TicketMenu Page which is a HTML page.

            :rtype: HttpResponse.

    """

    return render(request, 'Ticket/TicketMenu.html', {})

def genticket(request):
    """
            This method is used to generate ticket pdf for use.

            :param request: it's a FileResponse from user.

            :type request: FileResponse.

            :return: this method returns a Ticket.pdf which is a Pdf File.
            
            :rtype: FileResponse.

    """
    buf =io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica",14)

    ticdata = TicketSell.objects.all()
    Id = ticdata.last()
    s = Id.ticketNo
    a = str(s)
    d = Id.date
    ds = str(d)
    p = Id.total
    ps = str(p)
    lines = []

    lines.append("DHAKA     METRO    RAIL")
    lines.append("T I C K E T")
    lines.append("=====================================================")
    lines.append("Ticket No:")
    lines.append(a)
    lines.append(" ")
    lines.append("Source:")
    lines.append(Id.ticketSource)
    lines.append(" ")
    lines.append("Destination:")
    lines.append(Id.ticketDestination)
    lines.append(" ")
    lines.append("Date:")
    lines.append(ds)
    lines.append(" ")
    lines.append("Fare:")
    lines.append(ps)
    lines.append(" ")
    lines.append("=====================================================")


    for line in lines:
        textob.textLine(line)

    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='Ticket.pdf')

