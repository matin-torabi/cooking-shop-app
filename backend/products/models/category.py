from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Category(models.Model):
    name = models.CharField(max_length=100)
    discount = models.PositiveIntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    
    def __str__(self):
        return self.name