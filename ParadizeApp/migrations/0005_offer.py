# Generated by Django 5.0.2 on 2024-04-22 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ParadizeApp', '0004_ordermenu_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='')),
            ],
            options={
                'db_table': 'Offer',
            },
        ),
    ]