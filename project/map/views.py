from django.shortcuts import render
from django.http import HttpResponse

from main.models import SqData


def index(request):
    
    sightings = SqData.objects.all()[:100]
    
    context = {
        'sightings': sightings
    }
    
    return render(request,"map/index.html",context)

# Create your views here.
