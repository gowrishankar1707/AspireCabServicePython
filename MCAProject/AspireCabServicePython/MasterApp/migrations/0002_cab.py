# Generated by Django 4.1.6 on 2023-03-06 01:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MasterApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cabName', models.CharField(max_length=30)),
                ('noOfSeats', models.IntegerField()),
            ],
        ),
    ]
