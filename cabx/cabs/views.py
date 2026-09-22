from django.shortcuts import render
from .models import Cabs, Passanger
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    return render(request, "cabs/index.html",{
        "cabs" : Cabs.objects.all()
    })

def cab(request, cab_id):
    cab = Cabs.objects.get(pk=cab_id)
    return render(request, "cabs/cab.html",{
        "cab" : cab,
        "passangers" : cab.passangers.all(),
        "non_passangers" : Passanger.objects.exclude(cabs = cab).all()
    })

def book(request, cab_id):
    if request.method == "POST":
        cab = Cabs.objects.get(pk= cab_id)
        passanger = Passanger.objects.get(pk=request.POST["passanger"])
        passanger.cabs.add(cab)
        return HttpResponseRedirect(reverse("cab", args=(cab.id,)))