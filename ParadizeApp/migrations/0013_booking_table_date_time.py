# Generated by Django 5.0.2 on 2024-05-09 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ParadizeApp', '0012_alter_booking_table_date_alter_booking_table_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking_table',
            name='Date_Time',
            field=models.DateTimeField(null=True),
        ),
    ]
