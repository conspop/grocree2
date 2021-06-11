from django.db import models
from django.db.models.fields import BooleanField

class Ingredient(models.Model):
    name = models.CharField(max_length=20)
    isStaple = models.BooleanField()
    stapleAmount = models.CharField(max_length=20)

