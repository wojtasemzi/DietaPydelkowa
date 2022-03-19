from django.db import models

from ingredients.models import Ingredient

class Price(models.Model):
    ingredient_id = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    price = models.FloatField()
    currency_id = models.ForeignKey('Currency', on_delete=models.RESTRICT)
    quantity = models.FloatField()
    unit_id = models.ForeignKey('Unit', on_delete=models.RESTRICT)
    store_id = models.ForeignKey('Store', on_delete=models.RESTRICT)


class Currency(models.Model):
    currency = models.CharField(max_length=50)
    iso_4217 = models.CharField(max_length=3)


class Unit(models.Model):
    unit = models.CharField(max_length=20)
    abbreviation = models.CharField(max_length=5)


class Store(models.Model):
    store = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
