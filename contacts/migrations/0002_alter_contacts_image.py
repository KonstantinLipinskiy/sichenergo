# Generated by Django 4.2.17 on 2025-01-20 19:49

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='image',
            field=cloudinary.models.CloudinaryField(default='static/deps/img/trans.png', max_length=255, verbose_name='Зображення'),
        ),
    ]
