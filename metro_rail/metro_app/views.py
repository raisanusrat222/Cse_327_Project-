from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages

from django.contrib.auth import authenticate,login,logout
from metro_app.models import schedule_check
from metro_app.models import user_ticket
from metro_app.models import premium_ticket
from datetime import  datetime



# Create your views here.
def nav(request):
    diction= {}
    return render(request,'metro_app/nav.html',context=diction)
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('schedule')
    else:
         if request.method=='POST':
             username =request.POST.get('username')
             password =request.POST.get('password')

             user= authenticate(request, username=username, password=password)

             if user is not None:
                 login(request,user)
                 return redirect('schedule')
             else:
                messages.info(request,'Username or Password is incorrect')

    context= {}
    return render(request,'metro_app/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def schedule(request):
    diction= {}
    return render(request,'metro_app/schedule.html',context=diction)
def schedule_checks(request):
    schedule_check_list= schedule_check.objects.order_by ('route_id') 
    diction= {'schedule_check': schedule_check_list}
    return render(request,'metro_app/schedule_check.html',context=diction)
def adminPage (request):
    diction= {}
    return render(request,'metro_app/adminpage.html',context=diction)
def user_tickets (request):
    user_ticket_list= user_ticket.objects.order_by ('train_no') 
    diction= {'user_ticket': user_ticket_list}
    return render(request,'metro_app/user_ticket.html',context=diction)

def employee_tickets (request):
    diction= {}
    return render(request,'metro_app/employee_ticket.html',context=diction)


def premium_tickets(request):
    if 'q' in request.GET:
        q=request.GET['q']
        premium_ticket_list= premium_ticket.objects.filter(start_date_icontains=q)
    else:
        premium_ticket_list=premium_ticket.objects.all()
        premium_ticket_list= premium_ticket.objects.order_by ('user_name') 
        diction= {'premium_ticket': premium_ticket_list}
    return render(request,'metro_app/premium_ticket.html',context=diction)       


    
    



   
