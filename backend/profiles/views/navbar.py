# rest frame work:
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

# others
from drf_spectacular.utils import extend_schema

# serilizers:
from profiles.serializers.navbar import NavbarSerializer



class NavbarView(APIView):
    '''
    navbar Api
    
    This API hust for user info that show in frontent navbar
    
    Request Format:
    GET /profile/navbar/
    header{
        Authorazatons : Bearer <access token>}

    Response Format (Success):
    HTTP 200. OK
    {
        "status" : "USER_GROUP",
        "profile_image" : "profile URL",
        "cart_count" : 0 ,
    }
    
    
    Response Format (Error):
    HTTP 400 Bad Request
    {
        "status": "error",
        "message": "some message",

    }
    '''
    permission_classes = [IsAuthenticated]
    
    @extend_schema(request=NavbarSerializer , responses={200 : dict} , summary='اظلاعات کلی کاربر برای نوبار')
    def get(self, request, *args, **kwargs):
        user = request.user
        group = user.groups.first() 
        serializer = NavbarSerializer(request.user , context={"request": request})
        return Response({
            "user": serializer.data,
            "status": group.name if group else 'anonymouse',
        }, status=status.HTTP_200_OK)
        