# Generated by Django 5.1.7 on 2025-03-09 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yandex', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='yandexuser',
            name='_public_key',
            field=models.CharField(blank=True, db_column='public_key', default='', max_length=255),
        ),
    ]
