
# rest frame work:
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

# serializer:
from profiles.serializers.save_profile_pic import UpdateProfileSerializer

<<<<<<< HEAD
# others
from drf_spectacular.utils import extend_schema

class UpdateProfileView(APIView):
    """
    API view to update the user's profile image.

    Workflow:
        - If the user already has a profile image, delete the previous image before saving the new one.
        - Uses Pillow to convert the uploaded image to WebP format.
        - Delegates image processing to a Celery task for asynchronous handling.
        - Utilizes Redis for caching the processed image.

    This approach ensures efficient image handling and improves response times by offloading processing.
    """
    permission_classes = [IsAuthenticated]
    @extend_schema(request=UpdateProfileSerializer, responses={201 : dict} , summary=' اضافه یا عوض کردن پروفایل کاربر')
=======

# others
from drf_spectacular.utils import extend_schema


class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]
    @extend_schema(request=UpdateProfileSerializer, responses={200: str})
>>>>>>> d244423 (firs commit on linux)
    def post(self, request, *args, **kwargs):
        serializer = UpdateProfileSerializer(
            instance=request.user.profile,
            data=request.data,
            partial=True,
            context={'request': request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
<<<<<<< HEAD
        return Response({'message': 'اطلاعات با موفقیت بروزرسانی شد'}, status=status.HTTP_200_OK)
=======
        return Response({'detail': 'تصویر در صف پردازش قرار گرفت'}, status=status.HTTP_200_OK)
>>>>>>> d244423 (firs commit on linux)
