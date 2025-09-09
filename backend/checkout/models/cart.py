from django.contrib.auth import get_user_model
from django.db import models


class Cart(models.Model):
    user = models.OneToOneField(get_user_model(),on_delete=models.CASCADE,related_name="cart")
    
    def __str__(self):
        return str(self.user)