# Generated by Django 5.0.6 on 2024-09-15 04:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0014_event_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='date',
            new_name='eventDate',
        ),
    ]
