# Generated by Django 5.0.6 on 2024-09-29 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0019_post_isvideo_post_videourl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
