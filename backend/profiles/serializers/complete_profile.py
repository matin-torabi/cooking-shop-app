"""
After a user creates an account, they must complete their profile.
"""



# rest frame work:
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

# models:
from django.contrib.auth import get_user_model


class CompleteProfileViewSerializer(serializers.ModelSerializer):
    '''
    this serializer save user information such as first_name and last_name
    '''
    
    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name']
    
    # NOTE validate first and last name fields because we need these fields in future 
    
    def validate_first_name(self, value):
        
        if not value.strip():
            raise ValidationError("این فیلد نباید خالی باشد")
        if len(value) < 2:
            raise ValidationError("حداقل باید ۲ کاراکتر وارد کنید")
        
        if 50 < len(value):
            raise ValidationError("نام شما باید کمتر از ۵۰ کاراکتر باشد")
        
        return value

    def validate_last_name(self, value):
        
        if not value.strip():
            raise ValidationError("این فیلد نباید خالی باشد")
        if len(value) < 2:
            raise ValidationError("حداقل باید ۲ کاراکتر وارد کنید")
        
        if 50 < len(value):
            raise ValidationError("نام شما باید کمتر از ۵۰ کاراکتر باشد")
        return value
    
    

    def update(self, instance, validated_data):
        # save first and las name to db
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return instance
