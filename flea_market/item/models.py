from django.db import models

# Create your models here.

# category database class
class Category(models.Model):
    name=models.CharField(max_length=255)