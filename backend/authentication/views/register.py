# NOTE This file is responsible for registration.

# rest frame work:
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

# serializers:
from authentication.serializers.register import FirstStepRegisterSerializer , SecondStepRegisterSerializer

# others
from drf_spectacular.utils import extend_schema


class FirstStepRegisterView(APIView):
    '''
    First Step User Registration - Phone Number Validation and OTP Generation
    
    This API endpoint initiates the user registration process by validating an Iranian mobile
    number and generating a one-time password (OTP) for verification. A temporary session token
    is returned to securely reference this registration attempt in subsequent steps.
    
    Workflow:
    1. Receives an Iranian mobile phone number
    2. Validates the phone number format and uniqueness
    3. Generates a time-limited OTP code
    4. Sends the OTP to the provided phone number (via SMS/email)
    5. Returns a temporary session token for the next registration step
    
    Request Format:
    POST auth/register/step-one/
    {
        "phone_number": "09123456789"
    }
    
    Response Format (Success):
    HTTP 200 OK
    {
        "status": "success",
        "message": "OTP sent successfully",
        "temp_token": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    }
    
    Response Format (Error):
    HTTP 400 Bad Request
    {
        "status": "error",
        "message": "Invalid phone number format",
        
    }
    
    '''
    permission_classes = [AllowAny]
    @extend_schema(request=FirstStepRegisterSerializer , responses={200 : dict})
    def post(self , request , *args, **kwargs):
        serializer = FirstStepRegisterSerializer(data=request.data)
        
        serializer.is_valid(raise_exception=True)
        result = serializer.save()
        return Response(result, status=status.HTTP_200_OK)


    
class SecondStepRegisterView(APIView):
    '''
    Second Step User Registration - OTP Verification and Account Creation
    
    This API endpoint completes the user registration process by validating the
    one-time password (OTP) sent during the first registration step. Upon successful
    OTP verification, a new user account is created in the system.
    
    Workflow:
    1. Receives OTP code and session token from first registration step
    2. Validates the OTP against the stored value for the session
    3. If valid, creates a new user account with the provided credentials
    4. Returns authentication tokens or success confirmation
    
    Request Format:
    POST auth/register/step-two/
    {
        "temp_token": "string",
        "otp_code": "string"
    }
    
    Response Format (Success):
    HTTP 201. OK
    {
        "status": "success",
        "message": "User registered successfully",
        "refresh" : "refresh token"
        "access" : "access token"
    }
    
    
    Response Format (Error):
    HTTP 400 Bad Request
    {
        "status": "error",
        "message": "Invalid OTP code",

    }
    '''
    @extend_schema(request=SecondStepRegisterSerializer , responses={201 : dict})
    def post(self , request , *args, **kwargs):
        serializer = SecondStepRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = serializer.save()
        return Response(result, status=status.HTTP_201_CREATED)

