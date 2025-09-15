from rest_framework import serializers

from django.contrib.auth import get_user_model

class UserSerializer(serializers.SerializerMethodField):
    class Meta:
        model = get_user_model()
        fileds = '__all__'