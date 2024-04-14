from django.shortcuts import render
from .models import Farmer
from .serializers import FarmerSerializer
from rest_framework import generics

# Create your views here.
class FarmerList(generics.ListCreateAPIView):
    queryset = Farmer.objects.all()
    serializer_class = FarmerSerializer
