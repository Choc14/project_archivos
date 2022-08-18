# Generated by Django 4.0.6 on 2022-08-17 23:49

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customers', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('iva', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('total', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
            ],
        ),
        migrations.CreateModel(
            name='DetailInvoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('quantity', models.IntegerField(default=0)),
                ('subtotal', models.DecimalField(decimal_places=2, default=0.0, max_digits=9)),
                ('invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='invoices.invoice')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.product')),
            ],
        ),
    ]