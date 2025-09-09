# NOTE This file is responsible for login.

# rest frame work:
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

# serializers:
from authentication.serializers.login import  FirstStepLoginSerializer , SecondStepLoginSerializer

# others
from drf_spectacular.utils import extend_schema



class FirstStepLoginView(APIView):

    '''
    First Step User login - Phone Number Validation and OTP Generation
    

    Workflow:
    1. Receives an Iranian mobile phone number
    2. Validates the phone number format and uniqueness
    3. Generates a time-limited OTP code
    4. Sends the OTP to the provided phone number (via SMS/email)

    
    Request Format:
    POST auth/login/step-one/

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
    @extend_schema(request=FirstStepLoginSerializer , responses={200 : dict} , summary='دریافت کد یک بار مصرف برای ورود')
    def post(self , request , *args, **kwargs):    
        serializer = FirstStepLoginSerializer(data=request.data)
    
        serializer.is_valid(raise_exception=True)
        result = serializer.save()
        return Response(result, status=status.HTTP_200_OK)





class SecondSteploginView(APIView):
    '''
    Second Step login - OTP Verification and Account Creation
   
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
    @extend_schema(request=SecondStepLoginSerializer, responses={201 : dict} , summary='تایید کد یک بار مصرف و ورود کاربر')

    def post(self , request , *args, **kwargs):
        serializer = SecondStepLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = serializer.save()
        return Response(result, status=status.HTTP_201_CREATED)
