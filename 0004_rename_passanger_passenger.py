# Generated by Django 4.2.7 on 2023-12-04 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_passanger'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Passanger',
            new_name='Passenger',
        ),
    ]
