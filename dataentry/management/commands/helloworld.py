from django.core.management.base import BaseCommand


# Command is: python manage.py helloworld
class Command(BaseCommand):
    help = "Prints hello world"

    def handle(self, *args, **options):
        # write the logic in here
        self.stdout.write("Hello world")
