import csv
from django.core.management.base import BaseCommand
import datetime
from utils import search_for_model


# command is: python manage.py exportdata model_name
class Command(BaseCommand):
    help = 'Export data from the database to a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('model_name', type=str, help='Model name')

    def handle(self, *args, **options):
        model_name = options['model_name'].capitalize()

        # Search all the apps for the model name given
        model = search_for_model(model_name)

        # Fetch the data from the model
        data = model.objects.all()

        # Generate the timestamp of current data and time
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S")

        # define the csv file name/path
        file_path = f'exported_{model_name}_data_{timestamp}.csv'

        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)

            # write the csv header
            # we want to write the field names of the model
            writer.writerow([field.name for field in model._meta.fields])

            # write data rows
            for dt in data:
                writer.writerow([getattr(dt, field.name) for field in model._meta.fields])

        self.stdout.write(self.style.SUCCESS('Data exported successfully'))
