# Generated by Django 5.0.6 on 2024-10-16 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_rename_videourl_post_videoid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enquiry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=120)),
                ('studentCount', models.IntegerField()),
                ('studentGender', models.CharField(max_length=30)),
                ('tutorType', models.CharField(max_length=20)),
                ('subject', models.CharField(default='N.A', max_length=120)),
                ('grade', models.CharField(default='N.A', max_length=120)),
                ('language', models.CharField(default='N.A', max_length=120)),
                ('level', models.CharField(default='N.A', max_length=120)),
                ('availableTime', models.TextField()),
                ('learningStyle', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=250)),
                ('note', models.TextField()),
                ('date', models.DateField(auto_now=True)),
                ('isVideo', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'enquiries',
            },
        ),
    ]
