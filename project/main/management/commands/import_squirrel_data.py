from django.core.management.base import BaseCommand, CommandError

from django.apps import apps
# from django.db.models import sqdata

import csv

class Command(BaseCommand):
    help = 'Imports csv data from the given path'
    
    def add_arguments(self, parser):
        parser.add_argument('path', type = str, help = 'Path of the csv file with data')    

    def handle(self, *args, **kwargs ):
        path = kwargs['path']
        
        # if not path.name.endswith('.csv'):
        #     raise CommandError('Not a csv file')
        
        _model = apps.get_model('main','sqdata')

                 
        with open(path, mode ='r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',', quotechar='|')
            header = next(reader)
            header = [header.lower().replace(" ","_").replace("/","_") for header in header]          
            for row in reader:
                _object_dict = {key: value for key, value in zip(header, row)}
                _model.objects.create(**_object_dict)
            