# Generated by Django 4.0.6 on 2023-04-18 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('InformationSystem', '0007_alter_alert_city'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='title',
            field=models.CharField(blank=True, choices=[('Agression', 'Agression'), ('Viol', 'Viol'), ('Omisside', 'Omisside'), ('Viole', 'Viole'), ('Incendie', 'Incendie'), ('Inondation', 'Inondation')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='alertlist',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]