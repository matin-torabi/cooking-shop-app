# views
from products.views.product import ProductView
from products.views.product_page import ProductPageView
from django.urls import path



urlpatterns = [
    path('list/', ProductView.as_view(), name='products'),
    path('page/<slug:slug>/', ProductPageView.as_view(), name='product-page'),

]
