from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required 

from .models import Premium_Member
from django.contrib.auth.models import User
from .forms import PM_RegForm
from datetime import  timedelta, datetime
from django.utils import timezone
 


# Create your views here.
def nav(request):
    diction= {}
    return render(request,'metro_app/nav.html',context=diction)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('PremiumPage')
    else:
         if request.method=='POST':
             username =request.POST.get('username')
             password =request.POST.get('password')

             user= authenticate(request, username=username, password=password)

             if user is not None:
                 login(request,user)
                 return redirect('PremiumPage')
             else:
                messages.info(request,'Username or Password is incorrect')

    context= {}
    return render(request,'metro_app/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')




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
   

@login_required
def PremiumPage(request):

    current_user = request.user
    user_name = current_user.username

    info = Premium_Member.objects.get(User_Name = user_name)

    Edate = info.Start_Date 

    if info.Package == 'Monthly-1000 BDT':
        Edate = Edate + timedelta(days = 30)
        
    if info.Package == 'Half Yearly-4500 BDT': 
        Edate = Edate + timedelta(days = 180)
    if info.Package == 'Yearly-8000 BDT':
         Edate = Edate + timedelta(days = 365) 

    if request.method == 'POST':
        if request.POST.get('card'):
            if  info.Card_Status != 'applied for card':
                info.Card_Status = request.POST.get('card')
                info.save()
            else:
                messages.error(request,'already appied for card')

        if request.POST.get('rpac') or request.POST.get('pay'):
            s = request.POST.get('pay')
            if request.POST.get('rpac'):
                info.Package =  info.Package                
                info.save()  
                return redirect('PremiumPage') 
            else:
                messages.error(request,'nothing')

            if s == 'none':
                 messages.error(request,'nothing')
            else:    
                info.Package = request.POST.get('pay')                    
                info.save()
                return redirect('PremiumPage')
                
        
     

    context = {'info': info, 'Edate': Edate}

    return render (request, 'metro_app/premium member page.html', context)