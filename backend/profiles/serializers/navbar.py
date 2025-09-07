# rest frame work:
from rest_framework import serializers

# models:
from django.contrib.auth import get_user_model

User = get_user_model()

class NavbarSerializer(serializers.ModelSerializer):
   """
    Serializer for the navigation bar (navbar).

    This serializer is used to provide only the essential data needed
    to render the navbar across the website. It avoids sending
    unnecessary details to keep the response lightweight and fast.

    Fields returned:
        - profile_image (str | null): Absolute URL to the user's profile image.
          Returns deafult profile if no image is set.
        - cart_count (int): The total number of products currently in the user's cart.
   """
    
   profile_image = serializers.SerializerMethodField()
   cart_count = serializers.SerializerMethodField()

   class Meta:
      model = User
      fields = ['username', 'first_name', 'last_name', 'profile_image' , 'cart_count']

   def get_profile_image(self, obj):
<<<<<<< HEAD
        request = self.context.get("request")
        if obj.profile.image:
            return request.build_absolute_uri(obj.profile.image.url)
        return request.build_absolute_uri('/media/ananymouse/ananymouse.jpg/')
=======
      request = self.context.get("request")
    
    
      if hasattr(obj, 'profile') and obj.profile.image:
        return request.build_absolute_uri(obj.profile.image.url)
    
    
      default_url = '/media/profiles/profile.png'
      return request.build_absolute_uri(default_url)
>>>>>>> d244423 (firs commit on linux)

   def get_cart_count(self, obj):
      return 10
      #   return obj.cart.items.count() if hasattr(obj, "cart") else 0