from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from metro_app.models import schedule_check
from metro_app.models import TicketSell
from metro_app.models import employee_ticket


from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 

from django.contrib.auth.forms import UserCreationForm


from .models import PremiumMember, Employee
from django.contrib.auth.models import User
from .forms import RegForm
from datetime import  timedelta, datetime



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





# Create your views here.
def nav(request):
    """
        This method is a navigation bar of homepage.

        :param request: it's a HttpResponse from users.

        :type request: HttpResponse.

        :return: this method returns navigation bar which is a HTML page.

        :rtype: HttpResponse.

    """
    diction= {}
    return render(request,'metro_app/nav.html',context=diction)

def loginPage(request):
    """
        This method is used to view the login page.


        :param request: it's a HttpResponse from users.


        :type request: HttpResponse.

    
        :return: this method returns an adminpage,employee and premium member page which are a HTML page.

        :rtype: HttpResponse.

    """
    
    if request.user.is_authenticated:
        for instace in PremiumMember.objects.all():
            if request.user.username == instace.User_Name:
                return redirect('PremiumPage')
        for instance in Employee.objects.all():
            if request.user.username == instance.User_Name:
                return redirect('employeepage')
        for inst in User.objects.all():
            if request.user.username == inst.username:
                return redirect('adpage')   
        
      
    else:
         if request.method=='POST':
             username =request.POST.get('username')
             password =request.POST.get('password')

             user= authenticate(request, username=username, password=password)

             if user is not None:
                 login(request,user)
                 for instace in PremiumMember.objects.all():
                     if request.user.username == instace.User_Name:
                         return redirect('PremiumPage')
                 for instance in Employee.objects.all():
                     if request.user.username == instance.User_Name:
                          return redirect('employeepage')
                 for inst in User.objects.all():
                     if request.user.username == inst.username:
                           return redirect('adpage')            
               
             else:
                messages.info(request,'Username or Password is incorrect')

    context= {}
    return render(request,'metro_app/login.html',context)
def logoutUser(request):
    """
    This method is used to logout the user and redirect them to the login page.
    :param request: it's a HttpResponse from user.
    :type request: HttpResponse.
    :return: this method returns a login page which is a HTML page.
    :rtype: HttpResponse.
    """
    logout(request)
    return redirect('login')
    
    


def schedule_checks(request):
    """
    This method is used to display all the train schedule in schedule_checks page.
    :param request: it's a HttpResponse from user.
    :type request: HttpResponse.
    :return: this method returns schedule_chekcs page which is a HTML page.
    :rtype: HttpResponse.
    """
    schedule_check_list= schedule_check.objects.order_by ('route_id') 
    diction= {'schedule_check': schedule_check_list}
    return render(request,'metro_app/schedule_check.html',context=diction)

@login_required
def admin_pages (request):
    """

    This method is used to view the admin page.

    :param request: it's a HttpResponse from user.

    :type request: HttpResponse.

    :return: this method returns a search page which is a HTML page.

    :rtype: HttpResponse.


    """
    diction= {}
    return render(request,'metro_app/adminpage.html',context=diction)

def user_tickets (request):
    """

    This method is used to display the sell history of user_tickets and can search by date

    :param request: it's a HttpResponse from user.

    :type request: HttpResponse.

    :return: this method display and return the information of user tickets by serach

    :rtype: HttpResponse.


    """
    searchresult=TicketSell.objects.all()
    date=request.POST.get('date')
    if date != '' and date is not None:
        searchresult=searchresult.filter(date=date) 
        print(date)
        print(searchresult)
    return render(request,'metro_app/user_ticket.html',{"data":searchresult})
   

def employee_tickets (request):
    """

        This method is used to display the sell history of employee_tickets and can search by date

        :param request: it's a HttpResponse from user.

        :type request: HttpResponse.

        :return: this method display and return the information of employee tickets by serach

        :rtype: HttpResponse.

    """
    searchresult=employee_ticket.objects.all()
    date=request.POST.get('date')
    if date != '' and date is not None:
        searchresult=searchresult.filter(date=date) 
        print(date)
        print(searchresult)
    return render(request,'metro_app/employee_ticket.html',{"data":searchresult})
    

def premium_tickets(request):

    """
        This method is used to display the sell history of Premium Member and can search by start_date

        :param request: it's a HttpResponse from user.

        :type request: HttpResponse.

        :return: this method display and return the information of premium tickets by serach

    :rtype: HttpResponse.

    """
    
    searchresult=PremiumMember.objects.all()
    Start_Date=request.POST.get('date')
    if Start_Date != '' and Start_Date is not None:
        searchresult=searchresult.filter(Start_Date=Start_Date) 
        print(Start_Date)
        
        print(searchresult)
    return render(request,'metro_app/premium_ticket.html',{"data":searchresult})
   



   


    
    



 


# Create your views here.

def pregister(request):
    """
        This method is used to view the register page for premium member. A user can get
        registered as a premium member by filling the form with valid data.

        :param request: it's a HttpResponse from user.

        :type request: HttpResponse.

        :return: this method returns a premium member ragistration page which is a HTML page.

        :rtype: HttpResponse.
    """
    is_form = False
    if request.user.is_authenticated:
        return redirect('login')
    else:   
        form = RegForm()

        if request.method == 'POST':
            form = RegForm(request.POST) 
            obj = PremiumMember()

            first_name = request.POST['First Name']
            last_name = request.POST['Last Name']
            phone = request.POST['Phone Number']
            nid = request.POST['NID']
            card = request.POST['card']                  
            obj.First_Name = first_name
            obj.Last_Name =  last_name
            for instance in PremiumMember.objects.all():
                if phone == instance.Phone_Number:
                    messages.info(request, 'the phone number you entered already exists')
                    return redirect('pregister')
                else:    
                    obj.Phone_Number =  phone
            for instance1 in PremiumMember.objects.all():
                if nid == instance1.NID:
                    messages.info(request, 'the NID you entered already exists')
                    return redirect('pregister') 
                else:           
                    obj.NID = nid
            obj.Card_Num = card
            
            
            if request.POST.get('Pay_With'):              
                obj.Pay_With = request.POST.get('Pay_With')

            if request.POST.get('package-amount'):
                obj.Package = request.POST.get('package-amount') 
                
            if form.is_valid():
                obj.User_Name = form.cleaned_data['username']
                form.save()
                is_form = True 
            
            if is_form == True:
                obj.save()
                return redirect('login')
    
    context={'form': form}
    return render(request, 'metro_app/pregister.html', context)
   

def empregister(request):
    """
        This method is used to view the register page for Employee. An employee can be
        registered by filling the form with valid data.

        :param request: it's a HttpResponse from user.

        :type request: HttpResponse.

        :return: this method returns a employee ragistration page which is a HTML page.

        :rtype: HttpResponse.
    """
    is_form = False
    
    form = RegForm()

    if request.method == 'POST':
        form = RegForm(request.POST) 
        obj = Employee()

        first_name = request.POST.get('First_Name')
        last_name = request.POST.get('Last_Name')
        phone = request.POST.get('Phone_Number')
        nid = request.POST.get('NID')
        address = request.POST.get('Address')           
        obj.First_Name = first_name
        obj.Last_Name =  last_name
        for instance in Employee.objects.all():
            if phone == instance.Phone_Number:
                messages.info(request, 'the phone number you entered already exists')
                return redirect('empregister')
            else:    
                obj.Phone_Number =  phone
        for instance1 in Employee.objects.all():
            if nid == instance1.NID:
                messages.info(request, 'the NID you entered already exists')
                return redirect('empregister') 
            else:           
                obj.NID = nid
            obj.Address = address
                
        if form.is_valid():
            obj.User_Name = form.cleaned_data['username']
            form.save()
            is_form = True 
                          
            if is_form == True:
                obj.save()
                return redirect('login')

    context={'form': form}
    return render(request, 'metro_app/empregister.html', context)


@login_required
def premiumpage(request):
    """
        This method is used to view the premium member page. A premium member can check his
        current package also renew package and apply for card by logging in to his account.

        :param request: it's a HttpResponse from user.

        :type request: HttpResponse.

        :return: this method returns a employee ragistration page which is a HTML page.

        :rtype: HttpResponse.
    """
    current_user = request.user
    user_name = current_user.username

    info = PremiumMember.objects.get(User_Name = user_name)

    if request.method == 'POST':
        if request.POST.get('card'):
            if  info.Card_Status != 'applied for card':
                info.Card_Status = request.POST.get('card')
                info.save()
            else:
                messages.error(request,'already appied for card')

        if request.POST.get('package-amount'):
            p = request.POST.get('package-amount')
            if p == 'renew_package':
                info.Package =  info.Package                
                info.save()  
                return redirect('PremiumPage') 
            else:
                info.Package = request.POST.get('package-amount') 
                info.save()
                return redirect('PremiumPage')           

    Edate = info.Start_Date 

    if info.Package == 'Monthly-1000 BDT':
        Edate = Edate + timedelta(days = 30)
        
    if info.Package == 'Half Yearly-4500 BDT': 
        Edate = Edate + timedelta(days = 180)
    if info.Package == 'Yearly-8000 BDT':
         Edate = Edate + timedelta(days = 365)  

    context = {'info': info, 'Edate': Edate}

    return render (request, 'metro_app/premium member page.html', context)

@login_required
def employeepage(request):
    """
        This method is used to view the employee page. An employee can
        go to sell ticket page or ticket validation page from here.

        :param request: it's a HttpResponse from user.

        :type request: HttpResponse.

        :return: this method returns a employee ragistration page which is a HTML page.

        :rtype: HttpResponse.
    """
    context ={}
    return render (request, 'metro_app/employeepage.html', context)

@login_required
def TicketValid(request):
    """
        This method is used to view the ticket validation page for Employee. An employee
         can check if a ticket has been sold or not by searching with ticket no.

        :param request: it's a HttpResponse from user.

        :type request: HttpResponse.

        :return: this method returns a employee ragistration page which is a HTML page.

        :rtype: HttpResponse.
    """
    search = request.POST.get('search')
    ticket = TicketSell.objects.all() 
        
         
    if search != '' and search is not None:
        ticket = TicketSell.objects.filter(ticketNo=search)
        if ticket:
            messages.info(request, 'This ticket has been sold')
            context = {'ticket': ticket,}
            return render(request, 'metro_app/TicketValid.html', context)
        else:
            messages.info(request, 'This ticket has not been sold')               
            return render(request, 'metro_app/TicketValid.html')
    else:
            
        return render(request, 'metro_app/TicketValid.html')













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

