# Generated by Django 5.0.6 on 2024-10-16 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0023_rename_isvideo_enquiry_arranged'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enquiry',
            name='note',
            field=models.TextField(blank=True, null=True),
        ),
    ]
