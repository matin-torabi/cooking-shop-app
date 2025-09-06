"""
Serializer responsible for deleting a user's profile. 
If the user does not have a profile, it returns a default profile instead.
"""


# serializer:
from rest_framework import serializers

# model:
from profiles.models import Profile


class DeleteProfileSerializer(serializers.ModelSerializer):
    '''
    this serializer delete user's profile and then set default profile for user
    '''
    class Meta:
        model = Profile
        fields = ["image"]

    def validate(self, attrs):
        request = self.context.get('request')
        # # If the profile model does not perform correctly
        if not hasattr(request.user, 'profile'):
            raise serializers.ValidationError({'message': 'شما پروفایل ندارید' ,"status": "error",})
        return attrs

    def update(self, instance):

        # Clear the image field
        if instance.image:
            instance.image.delete(save=False)  # Delete the image file from storage
            instance.save()
        return instance
