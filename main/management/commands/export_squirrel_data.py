from django.core.management.base import BaseCommand, CommandError

from django.apps import apps
# from django.db.models import SqData

import csv

class Command(BaseCommand):
    help = 'Exports csv data from the given path'
    
    # raise error if the not a csv file
    def add_arguments(self, parser):
        parser.add_argument('path', type = str, help = 'Path of the csv file to write')    

    def handle(self, *args, **kwargs ):
        path = kwargs['path']
        if path[-4:] != '.csv':
            raise CommandError('Not a csv file')
        
        _model = apps.get_model('main','SqData')
        
        fields = _model._meta.get_fields() #retrieve column names and their types
        field_names = []
        for field in fields:
            field_names.append(field.attname)

        with open(path, mode ='w',newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter=',',quoting=csv.QUOTE_MINIMAL, quotechar='"')
            writer.writerow(field_names)
            
            for item in _model.objects.all():
                row_values = []
                for field_name in field_names:
                    value = getattr(item, field_name)
                    field = _model._meta.get_field(field_name)
                    #Boolean fields print as 0 or 1; 
                    #This converts to true/false string instead
                    if field.get_internal_type() == "BooleanField": 
                        if value == "0":
                            row_values.append(False)
                        else:
                            row_values.append(True)
                    else:
                        row_values.append(str(value))
                
                writer.writerow(row_values)
            print("Data sucessfully exported")
