# Generated by Django 4.2.4 on 2023-08-12 14:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0011_dailyvisitors_delete_daily_visitors'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyvisitors',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 12, 14, 26, 25, 627781, tzinfo=datetime.timezone.utc), null=True),
        ),
    ]
