# rest frame work:
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

# models:
from django.contrib.auth import get_user_model

# other:
from rest_framework_simplejwt.tokens import RefreshToken 
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import TokenError

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
    
    
    def validate(self, attrs):
        refresh = attrs.get('refresh')
        
        if not refresh:
            raise serializers.ValidationError({'message': 'مشکلی در پردازش پیش آمده!'})
        
        request = self.context.get('request')
        user = request.user
        
        User = get_user_model()
        user_ = User.objects.get(id=user.id)
        user_.is_active = False
        user_.save()
        
        
        
        return attrs

    def save(self, **kwargs):
        refresh = self.validated_data.get('refresh')

        # black the users jwt token
        try:
            token = RefreshToken(refresh)
            if not token.check_blacklist():
                token.blacklist()
            return ValidationError({"message": "شما با موفقیت خارج شدید"})
        except TokenError:
            return ValidationError({"message": "توکن قبلا بلاک شده"})
                
