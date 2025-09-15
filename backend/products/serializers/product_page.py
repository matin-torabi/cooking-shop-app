# models:
from products.models.product import Product

# serializers:
from rest_framework import serializers

class ProductPageSerializer(serializers.ModelSerializer):
    
    category = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    final_price = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    discount = serializers.SerializerMethodField()
    # weight = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ['name' , 'created_at', 'slug','description' , 'category' , 'image' , 'final_price' , 'price', 'discount','weight' ,'weight_type' , 'shelf_life_type' , 'shelf_life' ]

    def get_final_price(self, obj) -> int:
        # Calculates the final price of the product by applying the discount (if any)
        # and then returns the discounted price as an integer.  
        
        if obj.discount and obj.discount > 0:
            discount = obj.discount
        
        elif obj.category.exists():
            # get category discount if its not 0
            discount = max([cat.discount for cat in obj.category.all() if cat.discount > 0], default=0)
        
        else:
            discount = 0

        price = obj.price * (100 - discount) / 100 # calculate price with discount
        formatted = "{:,.0f}".format(price) # Format price with comma as thousands separator (every 3 digits)
        return formatted
    

    def get_image(self, obj) -> str:
        request = self.context.get('request')
        images = obj.images.all()

        return [
            request.build_absolute_uri(img.image.url) if request else img.image.url
            for img in images if img.image
                ]
    
    def get_price(self , obj) -> str:
        # Format price with comma as thousands separator (every 3 digits)
       
        price = obj.price
        formatted = "{:,.0f}".format(price)
        return formatted
    
    def get_discount(self, obj) -> str:    
        discount = obj.discount

        if discount > 0:
            return discount

        if obj.category.exists():
            return max([cat.discount for cat in obj.category.all() if cat.discount > 0], default=0)

        return 0
    
    def get_category(self, obj)-> str:
        if obj.category.name:
            return obj.category.name
        else:
            return 'بدون دسته بندی' 
        
        
    # def get_weight(self , obj):
        
    #     ...