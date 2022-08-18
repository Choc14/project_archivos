
# ID
import uuid

# ORM DE DJANGO
from django.db import models
from django.db.models.signals import pre_save

# SLUG
from django.utils.text import slugify

# SETTINGS OF PROJECT
from project_archivos.settings import MEDIA_URL, STATIC_URL

# TIEMPO
from datetime import datetime

# JSON
from django.forms import model_to_dict

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()    
    created_at = models.DateTimeField(default=datetime.now)


    def __str__(self):
        return self.title

    def toJSON(self):
        item = model_to_dict(self)
        item['created_at'] = self.created_at.strftime('%Y-%m-%d')
        return item

 

    

class Product(models.Model):
    title = models.CharField(max_length=25)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2, default=0.0)
    slug = models.SlugField(null=False, blank=False, unique=True)
    image = models.ImageField(upload_to='products/', null=True, blank='True')
    category = models.ManyToManyField(Category, blank=True)
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.title

    def toJSON(self):
        item = model_to_dict(self)
        item['price'] = format(self.price, '.2f')
        item['image'] = self.get_image()
        item['category'] = self.category.toJSON()
        item['created_at'] = self.created_at.strftime('%Y-%m-%d')
        return item

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL,'img/product/sin-imagen.png')
    
    


def set_slug(sender, instance, *args, **kwargs): 
    if instance.title and not instance.slug:
        slug = slugify(instance.title)

        while Product.objects.filter(slug=slug).exists():
            slug = slugify(
                '{}-{}'.format(instance.title, str(uuid.uuid4())[:8] )
            )

        instance.slug = slug

pre_save.connect(set_slug, sender=Product)
