# Generated by Django 5.0.2 on 2024-05-09 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ParadizeApp', '0014_remove_booking_table_date_time_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking_table',
            name='Date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booking_table',
            name='Time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
