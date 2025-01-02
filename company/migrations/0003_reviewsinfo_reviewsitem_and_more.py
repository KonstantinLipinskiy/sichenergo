# Generated by Django 4.2.17 on 2025-01-01 23:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_documentsinform_documentsitem_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewsInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Додатковий сервіс')),
                ('image', models.ImageField(upload_to='revies/', verbose_name='Зображення')),
                ('name', models.CharField(max_length=155, verbose_name='Короткий опис')),
                ('description', models.TextField(verbose_name='Опис')),
            ],
            options={
                'verbose_name': 'Сервіс',
                'verbose_name_plural': 'Сервіс (відгуки)',
            },
        ),
        migrations.CreateModel(
            name='ReviewsItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=155, verbose_name='Назва компанії')),
                ('image', models.ImageField(upload_to='revies/', verbose_name='Зображення')),
                ('description', models.TextField(verbose_name='Опис')),
                ('name', models.CharField(max_length=155, verbose_name='Трансформатор')),
                ('region', models.CharField(max_length=155, verbose_name='Регіон')),
            ],
            options={
                'verbose_name': 'Відгук',
                'verbose_name_plural': 'Відгуки',
            },
        ),
        migrations.AlterModelOptions(
            name='documentsinform',
            options={'verbose_name': 'Подію', 'verbose_name_plural': 'Події (Документи)'},
        ),
        migrations.AlterField(
            model_name='documentsinform',
            name='title',
            field=models.CharField(max_length=155, verbose_name='Останні події'),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='title',
            field=models.CharField(max_length=155, verbose_name='Презентація'),
        ),
    ]