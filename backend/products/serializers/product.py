# models:
from products.models.product import Product

# serializers:
from rest_framework import serializers
from products.serializers.product_image import ProductImageSerializer
from products.serializers.category import CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    '''
    it returns all products and product's category
    '''
    category = CategorySerializer(many=True, read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)
    final_price = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'

    def get_final_price(self, obj) -> int:
        if obj.discount and obj.discount > 0:
            discount = obj.discount
        
        elif obj.category.exists():
            discount = max([cat.discount for cat in obj.category.all() if cat.discount > 0], default=0)
        
        else:
            discount = 0

        return obj.price * (100 - discount) // 100
