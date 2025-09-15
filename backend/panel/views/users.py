from rest_framework.generics import ListAPIView
# from rest_framework.permissions import ...
from django.contrib.auth import get_user_model

class UsersPanellView(ListAPIView):
    queryset = get_user_model().objects.all()
    permission_classes