from django.contrib.auth import get_user_model
from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

class Cart(models.Model):
    user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE,related_name="cart")
    
    def __str__(self):
        return str(self.user)
    
    
    
# class CartItem(models.Model):
#     cart = models.ForeignKey(Cart , on_delete=models.CASCADE , related_name='items')
    
#     # Generic Relation:
#     content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
#     object_id = models.PositiveIntegerField()
#     content_object = GenericForeignKey('content_type' , 'object_id ')
    
#     quantity = models.PositiveIntegerField(default=1)
    
#     def __str__(self):
#         return f'{self.content_object} - {self.quantity}'