from rest_framework.generics import ListAPIView
from authentication.core.permissions.admin import IsAdmin
from django.contrib.auth import get_user_model
from panel.pagination.pagination import PanelPagination
from drf_spectacular.utils import extend_schema
from panel.serializers.users import UserSerializer


@extend_schema(responses=UserSerializer,summary="لیست کاربران")
class UsersPanellView(ListAPIView):
    '''
    it returns all user
    '''
    queryset = get_user_model().objects.all().order_by('-id')
    permission_classes = [IsAdmin]
    pagination_class = PanelPagination
    serializer_class = UserSerializer