# Generated by Django 5.0.2 on 2024-05-06 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ParadizeApp', '0011_remove_foodcart_data_added_alter_foodcart_quantity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking_table',
            name='Date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='booking_table',
            name='Time',
            field=models.TimeField(blank=True),
        ),
    ]
