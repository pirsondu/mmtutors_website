# Generated by Django 5.0.6 on 2024-09-09 11:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_alter_category_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('excerpt', models.CharField(max_length=200)),
                ('image', models.ImageField(null=True, upload_to='images')),
                ('date', models.DateField(auto_now=True)),
                ('slug', models.SlugField(unique=True)),
                ('content', models.TextField(validators=[django.core.validators.MinLengthValidator(10)])),
                ('categories', models.ManyToManyField(to='website.category')),
            ],
        ),
    ]
