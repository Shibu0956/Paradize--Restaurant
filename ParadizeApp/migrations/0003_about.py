# Generated by Django 5.0.2 on 2024-04-14 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ParadizeApp', '0002_booking_table_chefs_demoorder_foodmenu_ordermenu_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='')),
            ],
            options={
                'db_table': 'About',
            },
        ),
    ]
