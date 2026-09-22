from django.shortcuts import render
from .models import Cabs

# Create your views here.
def index(request):
    return render(request, "cabs/index.html",{
        "cabs" : Cabs.objects.all()
    })

def cab(request, cab_id):
    cab = Cabs.objects.get(pk=cab_id)
    return render(request, "cabs/cab.html",{
        "cab" : cab
    })
