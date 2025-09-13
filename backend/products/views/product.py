# models:
from products.models.product import Product

# serializers:
from products.serializers.product import  ProductSerializer

# others
from drf_spectacular.utils import extend_schema

# rest frame work
from rest_framework import generics



class ProductView(generics.ListAPIView):
    """
    this API returns all products with paginate
    """
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer

    @extend_schema(responses=ProductSerializer(many=True),summary="لیست محصولات")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
