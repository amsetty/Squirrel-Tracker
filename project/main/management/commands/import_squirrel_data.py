from django.core.management.base import BaseCommand, CommandError

from django.apps import apps
# from django.db.models import SqData

import csv

class Command(BaseCommand):
    help = 'Imports csv data from the given path'
    
    def add_arguments(self, parser):
        parser.add_argument('path', type = str, help = 'Path of the csv file with data')    

    def handle(self, *args, **kwargs ):
        path = kwargs['path']
        
        # raise error if the imported file is not csv
        if path[-4:] != '.csv':
            raise CommandError('Not a csv file')
        
        _model = apps.get_model('main','SqData')
        
        # Delete the existing data in the model before importing new dataset
        _model.objects.all().delete()

                 
        with open(path, mode ='r') as csv_file:
            reader = csv.reader(csv_file, delimiter=',', quotechar='"')
            header = next(reader)
            header = [header.lower().replace(" ","_").replace("/","_") for header in header]          
            for row in reader:
                _object_dict = {key: value for key, value in zip(header, row)}
                _object_dict_fixed = {}
                for key, value in _object_dict.items():
                    if value.lower() == "true":
                        _object_dict_fixed[key] = True
                    elif value.lower() == "false":
                        _object_dict_fixed[key] = False
                    elif key == "date":
                        new_date = value[4:] + "-" + value[0:2] + "-" + value[2:4]
                        _object_dict_fixed[key] = new_date
                    else:
                        _object_dict_fixed[key] = value
                _model.objects.create(**_object_dict_fixed)
            print("Data sucessfully imported")
