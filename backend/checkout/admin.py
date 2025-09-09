from django.contrib import admin

from checkout.models.cart import Cart


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    '''
    this is for Cart
    '''
    # add your custom setting here
    pass

