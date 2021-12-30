from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required 

from .models import PremiumMember, Employee
from django.contrib.auth.models import User
from .forms import RegForm
from datetime import  timedelta, datetime

 


# Create your views here.
def nav(request):
    diction= {}
    return render(request,'metro_app/nav.html',context=diction)







def pregister(request):
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
    is_form = False
    if request.user.is_authenticated:
        return redirect('login')
    else:   
        form = RegForm()

        if request.method == 'POST':
            form = RegForm(request.POST) 
            obj = Employee()

            first_name = request.POST['First Name']
            last_name = request.POST['Last Name']
            phone = request.POST['Phone Number']
            nid = request.POST['NID']
            address = request.POST['Address']           
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

        if request.POST.get('rpac'):
                       
            info.Package =  info.Package                
            info.save()  
            return redirect('PremiumPage') 

        if request.POST.get('package-amount'):
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


def TicketValid(request):
    # if request.method=='POST':
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
