# this files is responsible to complete user's info


# rest frame work:
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# others
from drf_spectacular.utils import extend_schema

# models:
from profiles.serializers.complete_profile import CompleteProfileViewSerializer


class CompleteProfileView(APIView):
    '''
    after authentication user can save his first and last name.
    
    Request Format:
    POST /profile/complete/
    {
      "first_name": "string",
      "last_name": "string"
    }
    
    header{
        Authorazatons : Bearer <access token>
        }
    
    Response Format (Success):
    HTTP 200. OK
    {
        "status": "success",
        "message": "string",
        "result": "string",

    }
    
    
    Response Format (Error):
    HTTP 400 Bad Request
    {
        "status": "error",
        "message": "string",
    }
    '''
    permission_classes = [IsAuthenticated]
    @extend_schema(request=CompleteProfileViewSerializer, responses={200: str} , summary='تکمیل پروفایل')
    def post(self, request, *args, **kwargs):
        serializer = CompleteProfileViewSerializer(instance=request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"status":"success" ,'result':serializer.data, "message":"اظلاعات با موفیقت ذخیره شد"}, status=status.HTTP_200_OK)