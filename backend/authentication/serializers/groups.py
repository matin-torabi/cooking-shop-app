

# rest frame work:
from rest_framework import serializers
from rest_framework.exceptions import ValidationError


# models:
from django.contrib.auth import get_user_model

from authentication.core.groups.group_manager import move_user_to_group



class AddToGropuSerializer(serializers.Serializer):
    phone_number = serializers.CharField()
    group_name = serializers.CharField()
    
    def validate(self, attrs):
        User = get_user_model()
        group_name = attrs.get('group_name')
        phone_number = attrs.get('phone_number')
        
        if not group_name:
            raise ValidationError({'message' : 'اسم گروه به درستی فرستاده نشد'})
        if not phone_number:
            raise ValidationError({'message' : 'شماره تلفن کاربر به درستی ارسال نشده'})
        if not User.objects.filter(username=phone_number).exists():
            raise ValidationError({'message' : 'این شماره پیدا نشد یا این کاربر هنوز حساب کاربری ندارد'})
        
        return attrs
    def save(self):
        phone_number = self.validated_data['phone_number']
        group_name = self.validated_data['group_name']
        
        added_user = move_user_to_group(username=phone_number , group_name=group_name)
        print(added_user)
        
        return added_user
        
        
        
        
        