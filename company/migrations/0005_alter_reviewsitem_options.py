# Generated by Django 4.2.17 on 2025-01-11 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_alter_documentsinform_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviewsitem',
            options={'ordering': ['-id'], 'verbose_name': 'Відгук', 'verbose_name_plural': 'Відгуки'},
        ),
    ]