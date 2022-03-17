from django.views.generic import ListView
from django.shortcuts import render

from ingredients import models


class Ingredients(ListView):
    model = models.Ingredient
    context_object_name = 'objects'
    template_name = 'list.html'
