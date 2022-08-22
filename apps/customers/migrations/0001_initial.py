# Generated by Django 4.0.6 on 2022-08-22 04:25

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_city', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Id',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_type', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=25)),
                ('last_name', models.CharField(max_length=25)),
                ('addres', models.CharField(max_length=75)),
                ('phone_number', models.CharField(max_length=8)),
                ('date_birth', models.DateField()),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.city')),
                ('id_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.id')),
            ],
        ),
    ]
