# NOTE: This file is a user-customized model

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator


class CustomUser(AbstractUser):
    '''
    
    Custom user model:
        - Username is used as phone number.
        - Default username field is kept but re-purposed.
    
    NOTE: i didn't delete default username feild , instead i use username as phone-number beacause its easier. XD
    '''
        
    username_validator = RegexValidator(
        regex=r'^0\d{10}$', # simple validation -> (if phone-number starts with 09 and has 11 char)
        message='Username must be exactly 11 digits.')

    username = models.CharField(max_length=11,unique=True,validators=[username_validator])
   
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        
    def __str__(self):
        return f"{str(self.username)}"
