from django.db import models

from meals.models import Meal
from ingredients.models import Tag


class Plan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    meals = models.ManyToManyField(through='Plan_Meal', to=Meal)
    tags = models.ManyToManyField(Tag)


class Plan_Meal(models.Model):
    plan_id = models.ForeignKey(Plan, on_delete=models.CASCADE)
    meal_id = models.ForeignKey(Meal, on_delete=models.CASCADE)
    day = models.ForeignKey('Day', on_delete=models.RESTRICT)
    order = models.IntegerField()


class Day(models.Model):
    name = models.CharField(max_length=15)
    order = models.IntegerField()
