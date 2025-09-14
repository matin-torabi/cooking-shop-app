from django.contrib import admin


# models
from products.models.product import Product 
from products.models.product_image import ProductImage
from products.models.category import Category

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    '''
    this is for Products
    '''
    prepopulated_fields = {'slug': ('name',)}
    pass


admin.site.register(ProductImage)



@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''
    this is for Category
    '''
    # add your custom setting here
    pass



