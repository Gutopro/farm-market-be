from django.db import models
from rest_framework import serializers


class BaseModel(models.Model):
    
    """ Defines base model to be inherited by other models """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Farmer(BaseModel):
    
    """ Defines the Farmer model which inherits from the base model """
    name = models.CharField(max_length=200)
    farm_name = models.CharField(max_length=200)
    email = models.CharField(max_length=200, unique=True)
    phone_number = models.CharField(max_length=200, unique=True)

