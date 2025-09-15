from django.utils.text import slugify


'''
Usage:
- in your model add this::


from authentication.core.slugs.slug import generate_slug

def save(self, *args, **kwargs):
        self.slug = generate_slug(self , name = self.name)
        super().save(*args, **kwargs)

'''


from slugify import slugify as py_slugify

def generate_slug(instance, name):
    """
    generate unique slug with transliteration (فارسی -> انگلیسی)
    """

    base_slug = py_slugify(name)
    slug = base_slug
    counter = 1

    while instance.__class__.objects.filter(slug=slug).exclude(pk=instance.pk).exists():
        slug = f"{base_slug}-{counter}"
        counter += 1

    return slug
