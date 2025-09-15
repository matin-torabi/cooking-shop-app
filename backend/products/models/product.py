from django.db import models
from products.models.category import Category
from authentication.core.slugs.slug import generate_slug
from django.core.validators import MaxValueValidator, MinValueValidator




class Product(models.Model):
    class Weight(models.TextChoices):
        GERAM = 'geram', 'geram'
        KILO = 'kilo', 'Kilo'

    name        = models.CharField(max_length=200)
    price       = models.IntegerField(default=0)
    slug        = models.SlugField(unique=True, blank=True)
    created_at  = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True, blank=True)
    stock       = models.PositiveIntegerField(default=0)
    weight_type = models.CharField(max_length=10, choices=Weight.choices , default=Weight.GERAM)
    weight      = models.PositiveIntegerField(default=0)
    category    = models.ManyToManyField(Category, related_name='products', blank=True)
    discount    = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.name
    

    
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self , name = self.name)
        super().save(*args, **kwargs)
        
