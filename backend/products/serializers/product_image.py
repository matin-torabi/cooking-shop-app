# serializers:
from rest_framework import serializers

# models:
from products.models.product_image import ProductImage



class ProductImageSerializer(serializers.ModelSerializer):
    '''
    produc's images
    '''
    class Meta:
        model = ProductImage
        fields = '__all__'