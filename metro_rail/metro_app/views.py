from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from metro_app.models import schedule_check
from metro_app.models import user_ticket
from metro_app.models import employee_ticket
from metro_app.models import premium_ticket
from metro_app.models import Employee
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required 




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
        for instace in premium_ticket.objects.all():
            if request.user.username == instace.user_name:
                return redirect('scheck')
        for instance in Employee.objects.all():
            if request.user.username == instance.User_Name:
                return redirect('schedule')
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
                 for instace in premium_ticket.objects.all():
                     if request.user.username == instace.user_name:
                         return redirect('scheck')
                 for instance in Employee.objects.all():
                     if request.user.username == instance.User_Name:
                          return redirect('schedule')
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
    
    

def schedule(request):
    diction= {}
    return render(request,'metro_app/schedule.html',context=diction)
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
def adminPage (request):
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
    searchresult=user_ticket.objects.all()
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
        This method is used to display the sell history of premium_tickets and can search by start_date

        :param request: it's a HttpResponse from user.

        :type request: HttpResponse.

        :return: this method display and return the information of premium tickets by serach

    :rtype: HttpResponse.

    """
    
    searchresult=premium_ticket.objects.all()
    start_date=request.POST.get('date')
    if start_date != '' and start_date is not None:
        searchresult=searchresult.filter(start_date=start_date) 
        print(start_date)
        
        print(searchresult)
    return render(request,'metro_app/premium_ticket.html',{"data":searchresult})
   



   


    
    



   
