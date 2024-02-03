from django.core.management.base import BaseCommand
from dataentry.models import Student


class Command(BaseCommand):
    help = 'Insert data to the database'

    def handle(self, *args, **kwargs):

        existing_record = Student.objects.filter(roll_no=10).exists()

        if not existing_record:
            self.stdout.write(self.style.SUCCESS('Data inserted successfully'))
            Student.objects.create(roll_no=10, name='Bill', age=24)
        else:
            self.stdout.write(self.style.WARNING(''))
