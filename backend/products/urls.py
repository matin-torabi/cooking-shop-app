# views
from products.views.product import ProductView
from django.urls import path



urlpatterns = [
    # Registration endpoints
    path('list/', ProductView.as_view(), name='product')

]
