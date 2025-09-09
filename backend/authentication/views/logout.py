
# rest frame work:
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# others
from drf_spectacular.utils import extend_schema

# serializer:
from authentication.serializers.logout import LogoutSerializer


class LogoutView(APIView):
    '''
    this API endpoint can block access token.
    
    
    Request Format:
    DELETE auth/auth/logout/

    header
    {
        
        Authorazatons : Bearer <access token>
        
    }

    Response Format (Success):
    HTTP 200. OK
    {
        
        "message": "str",
        
    }
    
    
    Response Format (Error):
    HTTP 400 Bad Request
    {
        
        "message": "str",

    }
    
    '''
    permission_classes = [IsAuthenticated]
    @extend_schema(request=LogoutSerializer , responses={200 : dict} , summary='بلاک کردن توکن access')
    def delete(self, request, *args, **kwargs):
        serializer = LogoutSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'result':serializer.data , 'message': 'شما از حساب خود خارج شدید'}, status=status.HTTP_200_OK)
