from django.db import models
from django.utils.translation import gettext as _

class sqdata(models.Model):
    x = models.FloatField(
        max_length = 25,
        help_text=_('Longitude coordinate for squirrel sighting point'),
    )
    
    y = models.FloatField(
        max_length= 25,
        help_text=_('Latitude coordinate for squirrel sighting point'),
    )
    
    unique_squirrel_id = models.CharField(
        max_length= 40,
        help_text= _('Hectare ID" + "Shift" + "Date" (MMDD) + "Hectare Squirrel Number.'),
    )
    
    hectare = models.CharField(
        max_length= 20,
        help_text= _('ID tag derived from hectare grid'),
    )
        
    shift = models.CharField(
        max_length= 20,
        help_text= _('Value is either "AM" or "PM," to communicate whether the sighting session occurred in the morning or late afternoon'),
    )
    
    date = models.IntegerField(
        max_length= 20,
        help_text= _('Sighting date')
    )
    
    hectare_squirrel_number = models.IntegerField(
        max_length= 30,
        help_text=_('Number within the chronological sequence of squirrel sightings for a discrete sighting session'),
        
    )
        
    age = models.CharField(
        max_length= 10,
        help_text= _('Value is either Adult or Juvenile.')
    )
    
    primary_fur_color = models.CharField(
        max_length= 30,
    )
    
    highlight_fur_color = models.CharField(
        max_length=30,
    )
    
    combination_of_primary_and_highlight_color = models.CharField(
        max_length=30,
    )
    
    color_notes = models.TextField(
        blank= True,
    )
    
    location = models.CharField(
        max_length=50,
    )
    
    above_ground_sighter_measurement = models.CharField(
        max_length=10,
    )
    
    specific_location = models.TextField(
        blank= True,
    )
    
    running = models.CharField( max_length=50)
    
    chasing = models.CharField( max_length=50)
    
    climbing = models.CharField( max_length=50)
    
    eating = models.CharField( max_length=50)
    
    foraging = models.CharField( max_length=50)
    
    other_activities = models.TextField(
        blank= True,
    )
    
    kuks = models.CharField( max_length=50)
    
    quaas = models.CharField( max_length=50)
    
    moans = models.CharField( max_length=50)
    
    tail_flags = models.CharField( max_length=50)
    
    tail_twitches = models.CharField( max_length=50)
    
    approaches = models.CharField( max_length=50)
    
    indifferent = models.CharField( max_length=50)
    
    runs_from = models.CharField( max_length=50)
    
    other_interactions = models.TextField(
        blank= True,
    )    
    
    lat_long = models.CharField(
        max_length=50,
    )
    
    def __str__(self):
        return self.unique_squirrel_id
    
        
    

# Create your models here.
