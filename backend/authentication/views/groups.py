# rest frame work:
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAdminUser

# serializers:
from authentication.serializers.login import  FirstStepLoginSerializer , SecondStepLoginSerializer

# others
from drf_spectacular.utils import extend_schema



class AddToGropuView(APIView):
    permission_classes = [IsAdminUser]
    def post(self, request, *args, **kwargs):
        ...
        
