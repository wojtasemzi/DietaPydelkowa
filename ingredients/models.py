from pyexpat import model
from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    energy_in_kcal = models.IntegerField()
    fat = models.FloatField()
    saturated_fat = models.FloatField()
    carbohydrate = models.FloatField()
    sugars = models.FloatField()
    fibre = models.FloatField()
    protein = models.FloatField()
    salt = models.FloatField()

    vitamins = models.ManyToManyField('Vitamin', blank=True)
    minerals = models.ManyToManyField('Mineral', blank=True)
    tags = models.ManyToManyField('Tag', blank=True)


class Vitamin(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)


class Mineral(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)


class Tag(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True)
