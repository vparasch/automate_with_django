from django.core.management.base import BaseCommand
from django.db import DataError
from utils import search_for_model
import csv


# Command is: python manage.py importdata file_path model_name


class Command(BaseCommand):
    help = 'Import data from CSV file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the CSV file')
        parser.add_argument('model_name', type=str, help='Model name')

    def handle(self, *args, **options):

        file_path = options['file_path']
        model_name = options['model_name'].capitalize()

        # Search all the apps for the model name given
        model = search_for_model(model_name)

        # Compare csv header with the model fields names
        model_fields = [field.name for field in model._meta.fields if field.name != 'id']  # exclude id field

        with open(file_path, 'r', encoding='utf8') as file:
            reader = csv.DictReader(file)
            csv_header = reader.fieldnames

            # Compare csv header with the model fields names
            if csv_header != model_fields:
                raise DataError(f'CSV file header does not match the {model_name} table field names')

            for row in reader:
                model.objects.create(**row)  # ** writes every column
            self.stdout.write(self.style.SUCCESS('Data inserted successfully'))
