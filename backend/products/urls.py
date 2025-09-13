# views
from products.views.product import ProductView
from django.urls import path



urlpatterns = [
    path('list/', ProductView.as_view(), name='product')

]
