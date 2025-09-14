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
    image = serializers.SerializerMethodField()
    final_price = serializers.SerializerMethodField()
    price  = serializers.SerializerMethodField()
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

        price = obj.price * (100 - discount) / 100
        formatted = "{:,.0f}".format(price)
        return formatted
    
    def get_image(self, obj):
        first_image = obj.images.first()
        if first_image and first_image.image:
            return first_image.image.url
        return None
    
    
    def get_price(self , obj):
        price = obj.price
        formatted = "{:,.0f}".format(price)
        return formatted
