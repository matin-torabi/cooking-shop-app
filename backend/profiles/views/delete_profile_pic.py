# this file is responsible to delete user's profile


# rest frame work:
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# serializer:
from profiles.serializers.delete_profile_pic import DeleteProfileSerializer

# others
from drf_spectacular.utils import extend_schema


class DeleteProfileView(APIView):
    '''
    this API endpoint can delete user's profile:
    user can delete profile with this endpoint
    
    DELETE /profile/delete/
    header{
        Authorazatons : Bearer <access token>
        }
    
    Response Format (Success):
    HTTP 200. OK
    {
        
        "message": "string",
        
    }
    
    
    Response Format (Error):
    HTTP 400 Bad Request
    {
        "status": "error",
        "message": "string",
    }
    
    
    '''
    permission_classes = [IsAuthenticated]
    @extend_schema(request=DeleteProfileSerializer, responses={200 : dict} , summary='حذف پروفایل فعلی کاربر')
    def delete(self, request, *args, **kwargs):
        profile = request.user.profile  # assuming OneToOneField from User to Profile
        serializer = DeleteProfileSerializer(
            instance=profile,
            data=request.data,
            context={'request': request},
            partial=True  # allows partial update (only image)
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'پروفایل شما با موفقیت حذف شد' ,"status": "success",}, status=status.HTTP_200_OK)