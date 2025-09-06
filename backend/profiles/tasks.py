# NOTE this file is responsible to save profile images

"""
Celery task for profile image processing.

Features:
    - Caches the processed image in Redis.
    - Resizes the image to 400x400 pixels.
    - Converts the image to WebP format.
    - Uses BytesIO for efficient in-memory operations.
"""

# django:
from django.core.cache import cache
from django.core.files.base import ContentFile

# models:
from django.contrib.auth import get_user_model
from profiles.models import Profile

# other:
from PIL import Image
from io import BytesIO
from celery import shared_task
import os



@shared_task              # redis key
def save_profile(username, key, filename=None):
    """
    Celery task to save a user's profile image from Redis cache to the database.
    """
    try:

        User = get_user_model()
        user = User.objects.get(username=username)
        profile, created = Profile.objects.get_or_create(user=user)

        # image data
        data = cache.get(key)
        if not data:
            return {"status": "error", "message": "عکس در کش پیدا نشد"}

        # delete previous profile
        if profile.image and profile.image.name != 'profiles/profile.png':
            profile.image.delete(save=False)
            
        
        im = Image.open(BytesIO(data))
        im = im.convert('RGB')
        im = im.resize((400, 400))

        # save image in RAM
        buffer = BytesIO()
        im.save(buffer, format='WEBP')
        buffer.seek(0)
        
        # change format to webp NOTE--> its better for site speed 
        name, ext = os.path.splitext(str(filename))
        webp_filename = f"{name}.webp"
        
        # add profile to user
        profile.image.save(webp_filename, ContentFile(buffer.read()), save=True)

        # remove chached image
        cache.delete(key)

        return {"status": "success", "message": "عکس با موفقیت ذخیره شد", "path": profile.image.url}

    except User.DoesNotExist:
    
        return {"status": "error", "message": "کاربر پیدا نشد"}
    except Exception as e:

        return {"status": "error", "message": str(e)}
