
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from client.models import DailyVisitors
from datetime import time

@receiver(pre_save, sender=YourModel)
def reset_value_at_midnight(sender, instance, **kwargs):
    if instance.pk is None:  # This indicates a new instance is being created
        now = timezone.now()
        if now.time() == time(0, 0):
            instance.Daily_visitors = 0
