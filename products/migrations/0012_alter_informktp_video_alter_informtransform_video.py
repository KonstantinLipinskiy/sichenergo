# Generated by Django 4.2.17 on 2025-01-20 19:49

import cloudinary_storage.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_informktp_file_ol_alter_transformtm_file_tm_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='informktp',
            name='video',
            field=models.FileField(blank=True, null=True, storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='videos/', verbose_name='Відео'),
        ),
        migrations.AlterField(
            model_name='informtransform',
            name='video',
            field=models.FileField(blank=True, null=True, storage=cloudinary_storage.storage.RawMediaCloudinaryStorage(), upload_to='videos/', verbose_name='Відео'),
        ),
    ]