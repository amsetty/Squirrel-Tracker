from django.shortcuts import render
from django.http import HttpResponse

from main.models import sqdata


def index(request):
    
    sightings = sqdata.objects.all()[:100]
    
    context = {
        'sightings': sightings
    }
    
    return render(request,"map/index.html",context)

# Create your views here.
