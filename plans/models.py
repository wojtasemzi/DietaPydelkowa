from django.db import models


class Plan(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    #TODO: meals = models.ManyToManyField(through='Plan_Meal', to=Meal)