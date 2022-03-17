from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100, blank=False)
    description = models.TextField()
    energy_in_kcal = models.IntegerField(blank=False)
    fat = models.FloatField(blank=False)
    saturated_fat = models.FloatField(blank=False)
    carbohydrate = models.FloatField(blank=False)
    sugars = models.FloatField(blank=False)
    fibre = models.FloatField(blank=False)
    protein = models.FloatField(blank=False)
    salt = models.FloatField(blank=False)

    #TODO: vitamins Ingredient_Vitamin
    #TODO: minerals Ingredient_Mineral
    #TODO: tags Ingredient_Tag
