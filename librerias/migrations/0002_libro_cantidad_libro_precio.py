# Generated by Django 5.0.4 on 2024-04-14 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librerias', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='cantidad',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='libro',
            name='precio',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
