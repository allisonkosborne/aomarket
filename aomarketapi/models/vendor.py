from django.db import models

class Vendors(models.Model):
  name = models.CharField(max_length=55)
  product = models.CharField(max_length=55)