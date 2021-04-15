from django.db import models
from django.utils.translation import gettext as _

from django.forms import ModelForm

class SqData(models.Model):
    x = models.FloatField(
        max_length = 25,
        help_text=_('Longitude coordinate for squirrel sighting point'),
    )
    
    y = models.FloatField(
        max_length=25,
        help_text=_('Latitude coordinate for squirrel sighting point'),
    )
    
    unique_squirrel_id = models.CharField(
        max_length=40,
        help_text= _('Hectare ID" + "Shift" + "Date" (MMDD) + "Hectare Squirrel Number.'),
        unique=True,
    )
        
    shift = models.CharField(
        max_length= 20,
        help_text= _('Value is either "AM" or "PM," to communicate whether the sighting session occurred in the morning or late afternoon'),
        choices = (
            ('PM', 'PM'),
            ('AM', 'AM'),
        )
    )
    
    date = models.CharField(
        max_length=10,
        help_text= _('Sighting date (format: YYYY-MM-DD)')
    )
        
    age = models.CharField(
        max_length= 10,
        help_text= _('Value is either Adult or Juvenile.'),
        choices = (
            ('Adult', 'Adult'),
            ('Juvenile', 'Juvenile'),
            )
        )
    
    hectare = models.CharField(
        max_length= 20,
        blank=True,
        help_text= _('ID tag derived from hectare grid'),
    )
    
    hectare_squirrel_number = models.IntegerField(
        help_text=_('Number within the chronological sequence of squirrel sightings for a discrete sighting session'),
        blank=True,
        null=True,  # Allows storing empty values to the database (text fields do not need this because they are stored as empty strings)
    )

    primary_fur_color = models.CharField(
        max_length= 30,
        blank=True,
        help_text= _('Primary fur color is either Gray, Cinnamon, or Black.'),
        choices = (
            ('Gray', 'Gray'),
            ('Cinnamon', 'Cinnamon'),
            ('Black', 'Black')
            )
    )
    
    highlight_fur_color = models.CharField(
        max_length=30,
        blank=True,
        help_text= _('Fur highlights are either Gray, Cinnamon, or Black.'),
        choices = (
            ('Gray', 'Gray'),
            ('Cinnamon', 'Cinnamon'),
            ('Black', 'Black')
            )
    )
    
    combination_of_primary_and_highlight_color = models.CharField(
        max_length=30,
        blank=True,
        help_text= _('A combination of the previous two columns; this column gives the total permutations of primary and highlight colors observed.')
    )
    
    color_notes = models.TextField(
        blank= True,
        help_text= _('Sighters occasionally added commentary on the squirrel fur conditions. These notes are provided here.')
    )
    
    location = models.CharField(
        max_length=50,
        blank=True,
        help_text= _('Value is either "Ground Plane" or "Above Ground." Sighters were instructed to indicate the location of where the squirrel was when first sighted.'),
        choices = (
            ('Ground Plane', 'Ground Plane'),
            ('Above Ground', 'Above Ground'),
        )
    )
    
    above_ground_sighter_measurement = models.CharField(
        max_length=10,
        blank=True,
        help_text= _('For squirrel sightings on the ground plane, fields were populated with a value of “FALSE.”')
     )
    
    specific_location = models.TextField(
        blank= True,
        help_text= _('Sighters occasionally added commentary on the squirrel location. These notes are provided here.')
    )

    running = models.BooleanField(
        default=False,
        help_text= _('Squirrel was seen running.'),
        )

    chasing = models.BooleanField(
        default=False,
        help_text= _('Squirrel was seen chasing another squirrel.'),
        )
    
    climbing = models.BooleanField(
        default=False,
        help_text= _('Squirrel was seen climbing a tree or other environmental landmark.')
        )
    
    eating = models.BooleanField(
        default=False,
        help_text= _('Squirrel was seen eating.')
        )
    
    foraging = models.BooleanField(
        default=False,
        help_text= _('Squirrel was seen foraging for food.')
        )
    
    other_activities = models.TextField(
        blank= True,
    )
    
    kuks = models.BooleanField(
        default=False,
        help_text= _('Squirrel was heard kukking, a chirpy vocal communication used for a variety of reasons.')
        )
    
    quaas = models.BooleanField(
        default=False,
        help_text=_('Squirrel was heard quaaing, an elongated vocal communication which can indicate the presence of a ground predator such as a dog.')
        )
    
    moans = models.BooleanField(
        default=False,
        help_text=_('Squirrel was heard moaning, a high-pitched vocal communication which can indicate the presence of an air predator such as a hawk.')
        )
    
    tail_flags = models.BooleanField(
        default=False,
        help_text=_("Squirrel was seen flagging its tail. Flagging is a whipping motion used to exaggerate squirrel's size and confuse rivals or predators. Looks as if the squirrel is scribbling with tail into the air.")
        )
    
    tail_twitches = models.BooleanField(
        default=False,
        help_text=_('Squirrel was seen twitching its tail. Looks like a wave running through the tail, like a breakdancer doing the arm wave. Often used to communicate interest, curiosity.')
        )
    
    approaches = models.BooleanField(
        default=False,
        help_text=_('Squirrel was seen approaching human, seeking food.')
        )
    
    indifferent = models.BooleanField(
        default=False,
        help_text=_('Squirrel was indifferent to human presence.')
        )
    
    runs_from = models.BooleanField(
        default=False,
        help_text=_('Squirrel was seen running from humans, seeing them as a threat.')
        )
    
    other_interactions = models.TextField(
        blank= True,
        help_text=_('Sighter notes on other types of interactions between squirrels and humans.')
    )    
    
    lat_long = models.CharField(
        max_length=50,
        blank=True,
        help_text=_('Insert as "POINT (Latitude Value Longitude Value)"')
    )
    
    id = models.AutoField(primary_key=True)
    
    def __str__(self):
        return self.unique_squirrel_id

class SqUpdateForm(ModelForm):
    class Meta:
        model = SqData
        fields = [ 'x', 'y', 'unique_squirrel_id', 'shift', 'date', 'age' ]

class SqAddForm(ModelForm):
    class Meta:
        model = SqData
        fields = '__all__'

# Create your models here.
