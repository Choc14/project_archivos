# ORM DE DJANGO
from django.db import models

# JSON
from django.forms import model_to_dict

# Modelos
from apps.customers.models import Customer
from apps.products.models import Product

# Tiempo
from datetime import datetime

# Create your models here.
class Invoice(models.Model):
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.CASCADE)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    created_at = models.DateTimeField(default=datetime.now)


    def __str__(self):
        return '{}'.format(self.customer)

    def toJSON(self):
        item = model_to_dict(self)
        item['customer'] = self.customer.toJSON()
        item['subtotal'] = format(self.subtotal, '.2f')
        item['iva'] = format(self.iva, '.2f')
        item['total'] = format(self.total, '.2f')
        item['created_at'] = self.created_at.strftime('%Y-%m-%d')
       
        
        return item


class DetailInvoice(models.Model):
    invoice = models.ForeignKey(Invoice,blank=True, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product,blank=True, null=True, on_delete=models.CASCADE)
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    quantity = models.IntegerField(default=0)
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)


    def __str__(self):
        return '{}'.format(self.product)

 



