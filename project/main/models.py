from django.db import models
from django.utils.translation import gettext as _

from django.forms import ModelForm

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
        blank=True,
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

    running = models.BooleanField(default=False)

    chasing = models.BooleanField(default=False)
    
    climbing = models.BooleanField(default=False)
    
    eating = models.BooleanField(default=False)
    
    foraging = models.BooleanField(default=False)
    
    other_activities = models.TextField(
        blank= True,
    )
    
    kuks = models.BooleanField(default=False)
    
    quaas = models.BooleanField(default=False)
    
    moans = models.BooleanField(default=False)
    
    tail_flags = models.BooleanField(default=False)
    
    tail_twitches = models.BooleanField(default=False)
    
    approaches = models.BooleanField(default=False)
    
    indifferent = models.BooleanField(default=False)
    
    runs_from = models.BooleanField(default=False)
    
    other_interactions = models.TextField(
        blank= True,
    )    
    
    lat_long = models.CharField(
        max_length=50,
    )
    
    id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.unique_squirrel_id

class SqUpdateForm(ModelForm):
    class Meta:
        model = sqdata
        fields = [ 'x', 'y', 'unique_squirrel_id', 'shift', 'date', 'age' ]

class SqAddForm(ModelForm):
    class Meta:
        model = sqdata
        fields = '__all__'

# Create your models here.
