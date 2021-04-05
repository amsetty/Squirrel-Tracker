from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Max
from django.db.models import Count
from django.db.models import Min

from main.models import sqdata

def index(request):
    return HttpResponse("Hello, world!")

def stats(request):
    
    # Total Number of sightings
    number_of_sightings = sqdata.objects.count()
    
    # Distribution of age of the squirrels
    age = sqdata.objects.values('age').annotate(dist_count=Count('age')).order_by('-dist_count')[:]  
    
    # Top three primary fur colors of the squirrels
    fur = sqdata.objects.values('primary_fur_color').annotate(dist_count=Count('primary_fur_color')).order_by('-dist_count')[:3]

    # Top three Hectare with most number of sightings   
    hec = sqdata.objects.values('hectare').annotate(dist_count=Count('hectare')).order_by('-dist_count')[:3]
    
    # Durations of the sightings
    min_date =  sqdata.objects.all().aggregate(Min('date'))
    max_date =  sqdata.objects.all().aggregate(Max('date'))
    

    #max_date.get('date__max') 10202018
    #min_date.get('date__min') 10062018
    
    context = {
        'sightings': number_of_sightings,
        'ages': age,
        'furs': fur,
        'hectares' : hec,
        'minimum_date' : min_date,
        'maximum_date' : max_date,
    }
    
    # return HttpResponse(fur[0])
    return render(request,"sightings/stats.html",context)

