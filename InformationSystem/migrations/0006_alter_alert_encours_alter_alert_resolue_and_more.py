# Generated by Django 4.0.6 on 2023-04-17 22:10

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InformationSystem', '0005_alter_alert_autor_alter_alert_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='Encours',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='alert',
            name='Resolue',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='alert',
            name='due_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='alert',
            name='location',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, default=None, null=True, srid=4326),
        ),
    ]