from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.db.models import Max
from django.db.models import Count
from django.db.models import Min
from django.contrib import messages

from main.models import SqData, SqUpdateForm, SqAddForm

def index(request):
    sightings = SqData.objects.all()

    context = {
        'sightings': sightings
    }

    return render(request,"sightings/index.html",context)

def stats(request):
    
    # Total Number of sightings
    number_of_sightings = SqData.objects.count()
    
    # Distribution of age of the squirrels
    age = SqData.objects.values('age').annotate(dist_count=Count('age')).order_by('-dist_count')[:]  
    
    # Top three primary fur colors of the squirrels
    fur = SqData.objects.values('primary_fur_color').annotate(dist_count=Count('primary_fur_color')).order_by('-dist_count')[:3]

    # Top three Hectare with most number of sightings   
    hec = SqData.objects.values('hectare').annotate(dist_count=Count('hectare')).order_by('-dist_count')[:3]
    
    # Durations of the sightings
    min_date =  SqData.objects.all().aggregate(Min('date'))
    max_date =  SqData.objects.all().aggregate(Max('date'))
    

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

    sightings = SqData.objects.all()

    context = {
        'sightings': sightings
    }

    return render(request,"sightings/index.html",context)

def update(request, unique_squirrel_id):
    squirrel = get_object_or_404(SqData.objects.all(), unique_squirrel_id=unique_squirrel_id)
    
    if request.method == 'POST':
        form = SqUpdateForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            messages.info(request, 'Squirrel sighting updated successfully!')
            return HttpResponseRedirect('/sightings/' + unique_squirrel_id)

    if request.method == 'GET':
        form = SqUpdateForm(instance=squirrel)

    if squirrel.primary_fur_color == "Cinnamon":
        squirrel_color = "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Squirrel_posing.jpg/1200px-Squirrel_posing.jpg"
    elif squirrel.primary_fur_color == "Black":
        squirrel_color = "https://www.stcnature.org/rccms/wp-content/uploads/2019/11/BlackSquirrels_11-22-19-620x362.jpg"
    elif squirrel.primary_fur_color == "Gray":
        squirrel_color = "https://a4.pbase.com/g4/37/669537/2/60807049.GreySquirrel.jpg"
    else:
        squirrel_color = "https://i.guim.co.uk/img/media/87225a7774183af748486e42a2910690a34c637e/1030_573_4085_2455/master/4085.jpg?width=1200&height=1200&quality=85&auto=format&fit=crop&s=077110e9d5b31edcd785beb1c011ea78"
        
    context = {
        'form': form, 
        'squirrel_color': squirrel_color
    }   

    return render(request, "sightings/update.html", context)


def add(request):
    if request.method == 'POST':
        form = SqAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Squirrel sighting added successfully!')
            return HttpResponseRedirect('/sightings/add')
    
    if request.method == 'GET':
        form = SqAddForm()

    context = {
        'form': form
    }

    return render(request, "sightings/add.html", context)
