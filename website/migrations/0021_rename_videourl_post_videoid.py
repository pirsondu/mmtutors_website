# Generated by Django 5.0.6 on 2024-09-29 03:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_alter_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='videoUrl',
            new_name='videoId',
        ),
    ]