# Generated by Django 4.2.4 on 2023-08-21 15:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0012_alter_dailyvisitors_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyvisitors',
            name='date',
            field=models.DateField(blank=True, default=datetime.datetime(2023, 8, 21, 15, 26, 18, 723823, tzinfo=datetime.timezone.utc), null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='menu_link',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
