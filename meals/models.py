from django.db import models

from ingredients.models import Tag
from recipes.models import Recipe

class Meal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    recipes = models.ManyToManyField(Recipe)
    tags = models.ManyToManyField(Tag)
