from django.contrib import admin


# models
from products.models.product import Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''
    this is for Products
    '''
    # add your custom setting here
    pass

