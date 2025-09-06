"""
Serializer responsible for adding or updating a user's profile.

Workflow:
    - Uses Celery and Redis for asynchronous image processing.
    - Resizes the profile image to 400x400 pixels.
    - Converts the profile image to WebP format.
"""

# serializer:
from rest_framework import serializers


# django:
from django.core.cache import cache

# worker:
from profiles.tasks import save_profile

# other:
import uuid

# model:
from profiles.models import Profile

class UpdateProfileSerializer(serializers.ModelSerializer):
    """
    Serializer responsible for updating user profile image.

    This serializer handles the update process for profile data, including 
    caching the profile image in Redis for faster access and leveraging Celery 
    to perform asynchronous processing tasks related to the profile update.

    Key features:
    - Updates user profile fields.
    - Caches profile images in Redis to improve performance.
    - Uses Celery for async operations, such as image processing or notifications.

    """

    image = serializers.ImageField(write_only=True)

    class Meta:
        model = Profile
        fields = ["image"]


    def update(self, instance, validated_data):
        # profile image
        image = validated_data.get("image")
        if not image:
            return instance

        # redis key
        key = f"profile:{instance.user.username}:{uuid.uuid4()}"
        
        # Read an image file as binary data and store it in Redis (in-memory storage)
        cache.set(key, image.read(), timeout=750) # save image for 12.5 mins
        

        # send to celety task
        save_profile.delay(username=instance.user.username, key=key, filename=image.name)

        return instance
