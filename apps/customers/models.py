from django.db import models
from datetime import datetime

# Create your models here.
class City(models.Model):
    name_city = models.CharField(max_length=50)

    def __str__(self):
        return self.name_city

class Id(models.Model):
    id_type = models.CharField(max_length=25)

    def __str__(self):
        return self.id_type


class Customer(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    addres = models.CharField(max_length=75)
    phone_number = models.CharField(max_length=8)
    date_birth = models.DateField()
    city = models.ForeignKey(City, null=False, blank=False, on_delete=models.CASCADE)
    id_type = models.ForeignKey(Id, null=False, blank=False, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    

    def __str__(self):
        return self.first_name + " " + self.last_name