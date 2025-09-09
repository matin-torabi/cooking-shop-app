from rest_framework.pagination import PageNumberPagination
from rest_framework.views import Response

class ProductPagination(PageNumberPagination):
    page_size = 15
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
