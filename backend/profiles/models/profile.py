from django.contrib.auth import get_user_model
User = get_user_model()
from django.db import models


class Profile(models.Model):
    image = models.ImageField(verbose_name="پروفایل" , upload_to='profiles/' , default='profiles/profile.jpg',null=True , blank=True)
    user = models.OneToOneField(User , on_delete=models.CASCADE , related_name='profile')
    
    def __str__(self):
        return str(self.user)
    
