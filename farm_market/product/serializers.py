from rest_framework import serializers
from .models import Product

# Create your Serializer here.
class ProductSerializer(serializers.ModelSerializer):
    """ Defines Product model interaction """
    class Meta:
        model = Product
        fields = '__all__'
