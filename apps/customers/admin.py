from django.contrib import admin

from .models import Customer, City, Id

# Register your models here.
class Customer_Admin(admin.ModelAdmin):
    fields = ('first_name', 'last_name', 'addres', 'phone_number', 'date_birth', 'city', 'id_type')
    list_display = ('__str__', 'created_at')

admin.site.register(Customer, Customer_Admin)
admin.site.register(City)
admin.site.register(Id)