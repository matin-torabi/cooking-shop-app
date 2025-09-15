#NOTE This file handles the main page of the site and returns all products with pagination.


# models:
from products.models.product import Product

# serializers:
from rest_framework import serializers

class ProductSerializer(serializers.ModelSerializer):
    '''
    it returns all products and product's category

    Workflow:
    - If a category discount exists, return the category discount.
    - If the product has its own discount, return the product discount instead.
    '''
    category = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    final_price = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    discount = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        fields = ['name' , 'slug' , 'created_at' , 'description' , 'category' , 'image' , 'final_price' , 'price', 'discount']

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
        # A product can have multiple images.
        # This method only returns the first image of the product.
        # So the result will always be a single image (not all of them).
        first_image = obj.images.first()
        if first_image and first_image.image:
            request = self.context.get('request')
            if request:
                return request.build_absolute_uri(first_image.image.url)
            return first_image.image.url
        return None
    
    
    def get_price(self , obj) -> str:
        # Format price with comma as thousands separator (every 3 digits)
       
        price = obj.price
        formatted = "{:,.0f}".format(price)
        return formatted
    
    def get_discount(self, obj) -> str:  
        """
        Priority is given to the product.  
        Returns the product's discount if it exists; otherwise, returns the category's discount if available.
        """  
        discount = obj.discount

        if discount > 0:
            return discount

        if obj.category.exists():
            return max([cat.discount for cat in obj.category.all() if cat.discount > 0], default=0)

        return 0
    
    def get_category(self, obj) -> str:
        """
        Returns the category name if the product belongs to a category; 
        otherwise, returns a default message.
        """
        if obj.category.name:
            return obj.category.name
        else:
            return 'بدون دسته بندی' 