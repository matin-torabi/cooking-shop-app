# NOTE this is for login serializer

"""
Login system with two-step API authentication for scalability.

Step 1: Receives a phone number and returns an OTP (One-Time Password) and a temporary token.
Step 2: Receives the temporary token and OTP, validates them, and returns JWT tokens upon successful authentication.
"""

# rest frame work:
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

# django:
from django.core.cache import cache

# models:
from django.contrib.auth import get_user_model


# other:
import random
import uuid
from rest_framework_simplejwt.tokens import RefreshToken



class FirstStepLoginSerializer(serializers.Serializer):
    '''
    Parameters:
        - phone_number: A valid Iranian mobile number.

    This serializer validates the phone number format and generates a one-time-password (OTP).
    A UUID4 token is used to uniquely identify the OTP session, so the frontend doesn't need to
    resend the phone number for verification.
    '''
    
    phone_number = serializers.CharField(help_text="Enter a valid phone number")
    def validate(self ,attrs , *args, **kwargs):
        phone_number = attrs.get('phone_number')
        User = get_user_model()
        
        # phone validation:
        if not phone_number:
            raise ValidationError({'message' : "شماره موبایل نباید خالی باشد"})
        if len(phone_number) != 11:
            raise ValidationError({'message' : "شماره تلفن معتبر نیست"})
        if not phone_number:
            raise ValidationError({'message' : "این فیلد نباید خالی باشد"})
        if not phone_number.isdigit():
            raise ValidationError({'message':"شماره تلفن فقط باید شامل اعداد باشد"})
        if not phone_number.startswith("0"):
            raise ValidationError({'message':"شماره تلفن باید با 0 شروع شود"})
        if phone_number.startswith("+98"):
            raise ValidationError({'message':"الگوی شماره تلفن اشتباه هست"})
        if not User.objects.filter(username=phone_number).exists():
            raise ValidationError({'message':"این شماره ثبت نام نکرده است"})
            
        return attrs
    
    def create(self, validated_data):
        phone_number = validated_data["phone_number"]

        # if OTP exists already
        existing = cache.get(f"otp:phone:{phone_number}")
        if existing:
            return {
                "status": "error",
                "message": "کد تأیید ارسال شده هنوز معتبر است",
                'time' : cache.ttl(f"otp:phone:{phone_number}")
            }

        # generate temp_token and OTP
        otp = str(random.randint(100000, 999999))
        temp_token = str(uuid.uuid4())

        # save OTP in cache
        cache.set(
            f"otp:{temp_token}",
            {"phone_number": phone_number, "otp": otp},
            timeout=120  # 2 min
        )

        cache.set(
            f"otp:phone:{phone_number}",
            {"temp_token": temp_token},
            timeout=120 # 2 min
        )

        return {
            "status": "success",
            "message": "کد ۶ رقمی با موفقیت ارسال شد",
            "temp_token": temp_token,
            "otp_code": otp # BUG it just for test dont use it on production
        }



class SecondStepLoginSerializer(serializers.Serializer):
    """
    Second step of user registration process.
    
    Validates OTP code and temporary token received from first registration step,
    then creates a new user account upon successful validation.
    
    Process flow:
    1. User receives OTP and temp_token after initial registration request
    2. User submits both values to this endpoint for verification
    3. Upon successful validation, a new user account is created
    
    Note: Uses 'username' field to store phone_number value
    
    Expected input:
    - otp: One-time password received by user
    - temp_token: Temporary token received from first registration step
    
    Returns:
    - User authentication tokens upon successful registration
    - Validation errors if OTP or token are invalid/expired
    """
    temp_token = serializers.CharField()
    otp_code = serializers.CharField()

    def validate(self, attrs):
        temp_token = attrs.get("temp_token")
        otp_code = attrs.get("otp_code")

        data = cache.get(f"otp:{temp_token}")
        if not data:
            raise ValidationError({"message": "کد منقضی شده یا نامعتبر است"})

        real_otp = data.get("otp")
        phone_number = data.get("phone_number")

        if str(otp_code) != str(real_otp):
            raise ValidationError({"message": "کد تأیید نادرست است"})
 
        attrs["phone_number"] = phone_number
        return attrs

    def create(self, validated_data):
        phone_number = validated_data["phone_number"]
        temp_token = validated_data["temp_token"]

        # delete cache
        cache.delete(f"otp:{temp_token}")
        cache.delete(f"otp:phone:{phone_number}")

        User = get_user_model()
        user, created = User.objects.get_or_create(username=phone_number)

        # activate user
        user.is_active = True
        user.save()
        
        # make jwt tokens
        token = RefreshToken.for_user(user)
        return {
            "status": "success",
            "message": "کد با موفقیت تأیید شد",
            'refresh' : str(token),
            'access' : str(token.access_token),
            "phone_number": phone_number,
        }
        
