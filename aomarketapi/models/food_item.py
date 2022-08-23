from unicodedata import category
from django.db import models

class FoodItems(models.Model):
  """"Represents the aisles in the market/store"""
  name = models.CharField(max_length=55)
  category = models.CharField(max_length=50)
  price = models.DecimalField(max_digits=7,decimal_places=2)
  