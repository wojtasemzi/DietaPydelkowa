from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import ListView
from django.shortcuts import render

from ingredients import forms
from ingredients import models


class Ingredients(ListView):
    model = models.Ingredient
    context_object_name = 'objects'
    template_name = 'list.html'


class IngredientAdd(CreateView):
    model = models.Ingredient
    form_class = forms.IngredientAdd
    template_name = 'add.html'
    success_url = reverse_lazy('ingredients')
