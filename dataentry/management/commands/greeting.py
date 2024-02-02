from django.core.management.base import BaseCommand


# Command is: python manager.py greeting {name}
class Command(BaseCommand):
    help = 'Prints Hello {name}'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help='Specifies user name')

    def handle(self, *args, **kwargs):
        # write the logic
        # kwargs is basically a dictionary
        name = kwargs['name']
        greeting = f'Hello {name}'
        self.stdout.write(greeting)

        # types in red letters
        # self.stderr.write(greeting)

        # types in green letters
        # self.stdout.write(self.style.Success(greeting))

        # types in yellow letters
        # self.stdout.write(self.style.WARNING(greeting))
