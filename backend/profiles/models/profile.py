from django.conf import settings
from django.db import models

class Profile(models.Model):
<<<<<<< HEAD
    image = models.ImageField(verbose_name="پروفایل" , upload_to='profiles/' , default='profiles/ananymouse/ananymouse.jpg',null=True , blank=True)
    user = models.OneToOneField(User , on_delete=models.CASCADE , related_name='profile')
    
=======
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='profile'
    )
    image = models.ImageField(
        verbose_name="پروفایل",
        upload_to='profiles/',
        default='profiles/profile.png',
        null=True,
        blank=True
    )

>>>>>>> d244423 (firs commit on linux)
    def __str__(self):
        return str(self.user)