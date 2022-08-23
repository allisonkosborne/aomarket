from django.db import models

class Employees(models.Model):
  name = models.CharField(max_length=55)
  bio = models.CharField(max_length=50)
  