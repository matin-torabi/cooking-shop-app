from django.db import models
from authentication.core.slugs.slug import generate_slug



class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    slug = models.SlugField(unique=True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.TextField(null=True , blank=True)
    recipe = models.TextField(null=True , blank=True)
    stock = models.PositiveIntegerField()
    
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = generate_slug(self , name = self.name)
        super().save(*args, **kwargs)