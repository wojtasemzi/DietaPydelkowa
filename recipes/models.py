from django.db import models

from ingredients.models import Ingredient
from ingredients.models import Tag
from ingredients.models import Unit

class Recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    recipe = models.TextField()
    ingredients = models.ManyToManyField(through='Recipe_Ingredient', to=Ingredient)
    preparation_time = models.IntegerField()
    tags = models.ManyToManyField(Tag, blank=True)


class Recipe_Ingredient(models.Model):
    recipe_id = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()
    unit_id = models.ForeignKey(Unit, on_delete=models.RESTRICT)
