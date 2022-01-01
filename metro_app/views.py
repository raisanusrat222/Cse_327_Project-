from django.shortcuts import render
from django.http import HttpResponse
from metro_app.models import SellTicket
# Create your views here.
def home(request):
    diction = {}
    if request.method=="POST":
        source = request.POST['source']
        destinationto = request.POST['destinationto']
        name = request.POST['name']
        email = request.POST['email']
        date = request.POST['date']
        print(source, destinationto, name, email, date)
        home = SellTicket(source=source, destinationto=destinationto, name=name, email=email, date=date)
        home.save()
        print(" ticket has been sold")
    return render(request,'metro_app/sellticket.html', context=diction)

def AboutUs(request):
    diction = {}
    return render(request,'metro_app/AboutUs.html', context=diction)


