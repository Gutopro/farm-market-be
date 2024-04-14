from rest_framework import serializers
from .models import Farmer

# Serializer class for Farmer model
class FarmerSerializer(serializers.ModelSerializer):
    """ Defines Farmer model interaction """
    class Meta:
        model = Farmer
        fields = '__all__' 
