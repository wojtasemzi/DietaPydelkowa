from django.db import models

from meals.models import Meal


class Plan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    meals = models.ManyToManyField(through='Plan_Meal', to=Meal)


class Plan_Meal(models.Model):
    plan_id = models.ForeignKey(Plan)
    meal_id = models.ForeignKey(Meal)
    #TODO: day = models.ForeignKey('Day')
    order = models.IntegerField()


class Day(models.Model):
    name = models.CharField(max_length=15)
    order = models.IntegerField()
