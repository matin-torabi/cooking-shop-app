from django.db import models
from products.models.product import Product


class ProductImage(models.Model):
    image = models.ImageField(verbose_name="محصولات" , upload_to='products/' , null=True , blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    
    
    def __str__(self):
        return f'{str(self.product)}'