from django.contrib import admin

# Register your models here.
from .models import Product, Catagory


admin.site.register(Product)
admin.site.register(Catagory)