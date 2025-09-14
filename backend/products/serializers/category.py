# serializers:
from rest_framework import serializers

# models:
from products.models.category import Category



class CategorySerializer(serializers.ModelSerializer):
    '''
    category serializers
    '''
    class Meta:
        model = Category
        fields = ["name",]