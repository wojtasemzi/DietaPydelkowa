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


class Price(models.Model):
    ingredient_id = models.ForeignKey(Ingredient)
    price = models.FloatField()
    currency_id = models.ForeignKey('Currency')
    quantity = models.FloatField()
    unit_id = models.ForeignKey('Unit')
    store_id = models.ForeignKey('Store')


class Currency(models.Model):
    currency = models.CharField(max_length=50)
    iso_4217 = models.CharField(max_length=3)


class Unit(models.Model):
    unit = models.CharField(max_length=20)
    abbreviation = models.CharField(max_length=5)


class Store(models.Model):
    store = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
