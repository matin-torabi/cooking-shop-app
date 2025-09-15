# django
from django.db import models

# models:
from django.contrib.auth import get_user_model
User = get_user_model()


# NOTE I set default profile if user doesn't have prilfe:
class Profile(models.Model):
    image = models.ImageField(verbose_name="پروفایل" , upload_to='profiles/' , default='ananymouse/ananymouse.jpg',null=True , blank=True)
    user  = models.OneToOneField(User , on_delete=models.CASCADE , related_name='profile')
    
    def __str__(self):
        return str(self.user)
    
