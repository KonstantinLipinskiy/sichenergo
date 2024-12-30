# Generated by Django 4.2.17 on 2024-12-30 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_transformtmg_transformtmz_transformyz'),
    ]

    operations = [
        migrations.CreateModel(
            name='InformKTP',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Опитовий лист')),
                ('video', models.FileField(blank=True, null=True, upload_to='video/', verbose_name='Відео')),
                ('description', models.TextField(blank=True, verbose_name='Опис')),
                ('file_ol', models.FileField(upload_to='ol/', verbose_name='Файл для скачування')),
            ],
            options={
                'verbose_name': 'Опитувальний лист',
                'verbose_name_plural': 'Опитувальні листи',
            },
        ),
    ]
