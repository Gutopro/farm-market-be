from django.db import models
from farmer.models import Farmer

# Create your models here.
class BaseModel(models.Model):
    """ Defines the base model for other models """
    created_at =  models.DateTimeField(auto_now_add=True)
    updated_at =  models.DateTimeField(auto_now=True)

class Product(BaseModel):
    """ Defines Product model """
    name =  models.CharField(max_length=200)
    description =  models.CharField(max_length=200)
    category =  models.CharField(max_length=200)
    farmer = models.ForeignKey(Farmer, on_delete=models.CASCADE)
    location = models.CharField(max_length=200, null=True, blank=True)
