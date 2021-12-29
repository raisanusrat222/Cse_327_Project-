from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required 

from .models import Premium_Member, Employee
from django.contrib.auth.models import User
from .forms import PM_RegForm
from .forms import EM_RegForm
from datetime import  timedelta, datetime

 


# Create your views here.
def nav(request):
    diction= {}
    return render(request,'metro_app/nav.html',context=diction)







def pregister(request):
    c = False
    if request.user.is_authenticated:
        return redirect('login')
    else:   
        form = PM_RegForm()

        if request.method == 'POST':
            form = PM_RegForm(request.POST) 
            obj = Premium_Member()
                
            if form.is_valid():
                obj.User_Name = form.cleaned_data['username']
                form.save()
                c = True 
            
            First_name = request.POST['First Name']
            Last_name = request.POST['Last Name']
            phone = request.POST['Phone Number']
            nid = request.POST['NID']
            card = request.POST['card']

        
            
            obj.First_Name = First_name
            obj.Last_Name =  Last_name
            obj.Phone_Number =  phone
            obj.NID = nid
            obj.Card_Num = card
            
            
            if request.POST.get('Pay_With'):
                
                obj.Pay_With = request.POST.get('Pay_With')

            if request.POST.get('package-amount'):
                obj.Package = request.POST.get('package-amount')    
            if c == True:
                obj.save()
                return redirect('login')
    
    context={'form': form}
    return render(request, 'metro_app/pregister.html', context)
   

def empregister(request):
    c = False
    if request.user.is_authenticated:
        return redirect('login')
    else:   
        form = EM_RegForm()

        if request.method == 'POST':
            form = EM_RegForm(request.POST) 
            obj = Employee()
                
            if form.is_valid():
                obj.User_Name = form.cleaned_data['username']
                form.save()
                c = True 
            
            First_name = request.POST['First Name']
            Last_name = request.POST['Last Name']
            phone = request.POST['Phone Number']
            nid = request.POST['NID']
            address = request.POST['Address']

        
            
            obj.First_Name = First_name
            obj.Last_Name =  Last_name
            obj.Phone_Number =  phone
            obj.NID = nid
            obj.Address = address
               
            if c == True:
                obj.save()
                return redirect('login')

    context={'form': form}
    return render(request, 'metro_app/empregister.html', context)

@login_required
def PremiumPage(request):

    

    current_user = request.user
    user_name = current_user.username

    info = Premium_Member.objects.get(User_Name = user_name)

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
        # else:
        #     messages.error(request,'nothing')

        if request.POST.get('package-amount'):
            info.Package = request.POST.get('package-amount') 
            info.save()
            return redirect('PremiumPage')   

        # else:
        #     return redirect('PremiumPage')         
                
                     
 
    # info = Premium_Member.objects.get(User_Name = user_name)              

    Edate = info.Start_Date 

    if info.Package == 'Monthly-1000 BDT':
        Edate = Edate + timedelta(days = 30)
        
    if info.Package == 'Half Yearly-4500 BDT': 
        Edate = Edate + timedelta(days = 180)
    if info.Package == 'Yearly-8000 BDT':
         Edate = Edate + timedelta(days = 365)  

     

    context = {'info': info, 'Edate': Edate}

    return render (request, 'metro_app/premium member page.html', context)