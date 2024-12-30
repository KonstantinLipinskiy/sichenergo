# Generated by Django 4.2.17 on 2024-12-30 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_transformtm'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransformTmg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Потужність трансформаторів ТМГ та ТМЖГ')),
                ('image', models.ImageField(upload_to='img_tmg/', verbose_name='Креслення трансформаторів ТМГ та ТМЖГ')),
                ('file_tmg', models.FileField(upload_to='drawing_tmg/', verbose_name='Скачати креслення трансформаторів ТМГ та ТМЖГ')),
            ],
            options={
                'verbose_name': 'Трансформатор ТМГ та ТМЖГ',
                'verbose_name_plural': 'Трансформатори ТМГ та ТМЖГ',
            },
        ),
        migrations.CreateModel(
            name='TransformTmz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Трансформатори ТМЗ')),
                ('image', models.ImageField(upload_to='img_tmz/', verbose_name='Креслення трансформаторів ТМЗ')),
                ('file_tmz', models.FileField(upload_to='drawing_tmz/', verbose_name='Скачати креслення трансформаторів ТМЗ')),
            ],
            options={
                'verbose_name': 'Трансформатор ТМЗ',
                'verbose_name_plural': 'Трансформатори ТМЗ',
            },
        ),
        migrations.CreateModel(
            name='TransformYZ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Трансформатори серії Y/Z')),
                ('image', models.ImageField(upload_to='img_yz/', verbose_name='Креслення трансформаторів Y/Z')),
                ('file_yz', models.FileField(upload_to='drawing_yz/', verbose_name='Скачати креслення трансформаторів Y/Z')),
            ],
            options={
                'verbose_name': 'Трансформатор Y/Z',
                'verbose_name_plural': 'Трансформатори Y/Z',
            },
        ),
    ]
