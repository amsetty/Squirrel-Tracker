from django.shortcuts import render

from django.http import HttpResponse

from main.models import sqdata

def index(request):
    sightings = sqdata.objects.all()

    context = {
        'sightings': sightings
    }

    return render(request,"sightings/index.html",context)

def update(request, unique_squirrel_id):
    return HttpResponse("Hello squirrel " + unique_squirrel_id)
