from django.db import models
from products.models.category import Category
from authentication.core.slugs.slug import generate_slug
from django.core.validators import MaxValueValidator, MinValueValidator




class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField(default=0)
    slug = models.SlugField(unique=True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True , blank=True)
    recipe = models.TextField(null=True , blank=True)
    stock = models.PositiveIntegerField(default=0)
    category = models.ManyToManyField(Category , related_name='category')
    discount = models.PositiveIntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])

    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self , name = self.name)
        super().save(*args, **kwargs)