from django.core.management.base import BaseCommand
from client.models import DailyVisitors

class Command(BaseCommand):
    help = 'Reset a value to 0 at midnight'

    def handle(self, *args, **options):
        YourModel.objects.all().update(Daily_visitors=0)
        self.stdout.write(self.style.SUCCESS('Value reset to 0'))
