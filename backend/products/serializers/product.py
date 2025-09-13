# models:
from products.models.product import Product

# serializers:
from rest_framework import serializers
from products.serializers.category import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    '''
    it returns all products and product's category
    '''
    category = CategorySerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = '__all__'

