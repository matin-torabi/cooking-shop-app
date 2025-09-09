# models:
from products.models.product import Product

# serializers:
from products.serializers.product_page import ProductPageSerializer

# others
from drf_spectacular.utils import extend_schema

# rest frame work
from rest_framework import generics

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

@method_decorator(cache_page(60 * 15), name="dispatch")
@extend_schema(responses=ProductPageSerializer,summary="صفحه محصولات" , description='Receives a slug and returns the product associated with it.')
class ProductPageView(generics.RetrieveAPIView):
    serializer_class = ProductPageSerializer
    queryset = Product.objects.all()
    lookup_field = 'slug'
