from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.db.models import Max
from django.db.models import Count
from django.db.models import Min
from django.contrib import messages

from main.models import sqdata, SqUpdateForm, SqAddForm

def index(request):
    sightings = sqdata.objects.all()

    context = {
        'sightings': sightings
    }

    return render(request,"sightings/index.html",context)

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

    sightings = sqdata.objects.all()

    context = {
        'sightings': sightings
    }

    return render(request,"sightings/index.html",context)

def update(request, unique_squirrel_id):
    if request.method == 'POST':
        form = SqUpdateForm(request.POST)
        if form.is_valid():
            new_squirrel = form.save(commit=False)
            squirrel = get_object_or_404(sqdata.objects.all(), unique_squirrel_id=unique_squirrel_id)
            squirrel.x = new_squirrel.x
            squirrel.y = new_squirrel.y
            squirrel.unique_squirrel_id = new_squirrel.unique_squirrel_id
            squirrel.shift = new_squirrel.shift
            squirrel.date = new_squirrel.date
            squirrel.age = new_squirrel.age
            squirrel.save(update_fields=["x", "y", "unique_squirrel_id", "shift", "date", "age"])
            messages.info(request, 'Squirrel sighting updated successfully!')
            return HttpResponseRedirect('/sightings/' + unique_squirrel_id)
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        squirrel = get_object_or_404(sqdata.objects.all(), unique_squirrel_id=unique_squirrel_id)
        form = SqUpdateForm(instance=squirrel)

        context = {
            'form': form
        }   

        return render(request, "sightings/update.html", context)


def add(request):
    if request.method == 'POST':
        form = SqAddForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Squirrel sighting added successfully!')
            return HttpResponseRedirect('/sightings/add')
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    else:
        form = SqAddForm()

        context = {
            'form': form
        }

        return render(request, "sightings/add.html", context)
