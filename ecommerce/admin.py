from django.contrib import admin
from .models import Product
# Register your models here.
class AddProductList(admin.ModelAdmin):
    list_display = (
        'Name',
        'Slug',
        'Tags',
        'Price',
        'Des',
        'Date',
        'PImage'
    )

admin.site.register(Product,AddProductList)