from django.contrib import admin

from .models import Product # . means current directory

# Register your models here.
admin.site.register(Product)