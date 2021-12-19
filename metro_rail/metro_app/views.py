from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth import authenticate

from django.contrib.auth.forms import UserCreationForm

from .models import Premium_Member
from django.contrib.auth.models import User
from .forms import PM_RegForm


# Create your views here.
def nav(request):
    diction= {}
    return render(request,'metro_app/nav.html',context=diction)

    

def pregister(request):
        c = False
    # if request.user.is_authenticated:
    #     return redirect('login')
    # else:   
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
                # return redirect('login')
    
        context={'form': form}
        return render(request, 'metro_app/pregister.html', context)
   


def PremiumPage(request):
    context = {}

    return render (request, 'metro_app/premium member page.html', context)