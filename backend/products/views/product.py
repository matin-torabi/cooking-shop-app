# models:
from products.models.product import Product

# serializers:
from products.serializers.product import  ProductSerializer

# others
from drf_spectacular.utils import extend_schema

# rest frame work
from rest_framework import generics


from rest_framework.pagination import PageNumberPagination
from rest_framework.views import Response

class ProductPagination(PageNumberPagination):
    page_size = 2
    def get_paginated_response(self, data):
        total_items = self.page.paginator.count
        total_pages = (total_items + self.page_size - 1) // self.page_size
        return Response({
            'total_items': total_items,
            'total_pages': total_pages,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })

class ProductView(generics.ListAPIView):
    """
    this API returns all products with paginate
    """
    queryset = Product.objects.all().order_by('-id')
    serializer_class = ProductSerializer
    pagination_class = ProductPagination

    @extend_schema(responses=ProductSerializer(many=True),summary="لیست محصولات")
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
