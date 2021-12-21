from django.shortcuts import render
from .models import Trainfare
from .models import Complain
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






