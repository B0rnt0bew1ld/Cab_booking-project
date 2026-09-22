from django.shortcuts import render
from .models import Cabs

# Create your views here.
def index(request):
    return render(request, "cabs/index.html",{
        "cabs" : Cabs.objects.all()
    })

