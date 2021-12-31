from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    diction = {}
    return render(request,'metro_app/sellticket.html', context=diction)

def sellticket(request):
    form = forms.sellticket()

    if request.method == "Post":
        form = forms.sellticket(request.Post)
        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction = {'title': 'Ticket Form', "sellicket":form}
    print (diction)
    return render(request,'metro_app/sellticket.html', context=diction)
