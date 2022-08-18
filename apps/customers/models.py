
# ORM DE DJANGO
from django.db import models

# Tiempo
from datetime import datetime

# JSON
from django.forms import model_to_dict

# Create your models here.
class City(models.Model):
    name_city = models.CharField(max_length=50)

    def __str__(self):
        return self.name_city

    def toJSON(self):
        item = model_to_dict(self)
        return item

class Id(models.Model):
    id_type = models.CharField(max_length=25)

    def __str__(self):
        return self.id_type

    def toJSON(self):
        item = model_to_dict(self)
        return item

class Customer(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    addres = models.CharField(max_length=75)
    phone_number = models.CharField(max_length=8)
    date_birth = models.DateField()
    city = models.ForeignKey(City, null=False, blank=False, on_delete=models.CASCADE)
    id_type = models.ForeignKey(Id, null=False, blank=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=datetime.now)

    

    def __str__(self):
        return self.first_name + " " + self.last_name

    def toJSON(self):
        item = model_to_dict(self)
        item['date_birth'] = self.date_birth.strftime('%Y-%m-%d')
        item['city'] = self.city.toJSON()
        item['id_type'] = self.id_type.toJSON()
        item['created_at'] = self.created_at.strftime('%Y-%m-%d')
        return item