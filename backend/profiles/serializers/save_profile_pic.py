<<<<<<< HEAD
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
=======
import uuid
from django.core.cache import cache
from rest_framework import serializers
from profiles.models import Profile
from profiles.tasks import save_profile

class UpdateProfileSerializer(serializers.ModelSerializer):
>>>>>>> d244423 (firs commit on linux)
    image = serializers.ImageField(write_only=True)

    class Meta:
        model = Profile
        fields = ["image"]
<<<<<<< HEAD

    def update(self, instance, validated_data):
        # profile image
        image = validated_data.get("image")
        if not image:
            return instance

        # redis key
        key = f"profile:{instance.user.username}:{uuid.uuid4()}"
        # save image to redis
        cache.set(key, image.read(), timeout=300)
        
=======

    def update(self, instance, validated_data):
        image = validated_data.get("image")
        if not image:
            return instance

        # کلید یکتا برای ذخیره در Redis
        key = f"profile:{instance.user}:{uuid.uuid4()}"
        cache.set(key, image.read(), timeout=300)

        # ارسال تسک به Celery
        print(instance.user)
        save_profile.delay(username=instance.user.username, key=key, filename=image.name)
>>>>>>> d244423 (firs commit on linux)

        # send to celety task
        save_profile.delay(username=instance.user.username, key=key, filename=image.name)

        return instance
