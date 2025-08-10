from rest_framework.views import APIView
from rest_framework.response import Response

from products.models.product import Product
# from products.serializers.product import ProductSerializer
from rest_framework import serializers
# from products.models.product import Product


from rest_framework import generics


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'



class ProductView(generics.ListAPIView):
        queryset = Product.objects.all().order_by('-id')
        serializer_class = ProductSerializer
       

