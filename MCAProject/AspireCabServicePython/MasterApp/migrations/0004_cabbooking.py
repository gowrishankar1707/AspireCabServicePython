# Generated by Django 4.1.6 on 2023-03-20 15:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MasterApp', '0003_route'),
    ]

    operations = [
        migrations.CreateModel(
            name='CabBooking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shift', models.CharField(blank=True, max_length=10)),
                ('isCancelled', models.BooleanField(blank=True, default=False)),
                ('bookedDate', models.DateField(blank=True)),
                ('route', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MasterApp.route')),
                ('userRe', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='MasterApp.userregistration')),
            ],
        ),
    ]
