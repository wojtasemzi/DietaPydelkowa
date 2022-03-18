from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.shortcuts import render

from recipes import forms
from recipes import models


class Recipes(ListView):
    model = models.Recipe
    context_object_name = 'objects'
    template_name = 'list.html'


class RecipeAdd(CreateView):
    model = models.Recipe
    form_class = forms.RecipeAdd
    template_name = 'add.html'
    success_url = reverse_lazy('recipes')


class Recipe(DetailView):
    model = models.Recipe
    template_name = 'object.html'


class RecipeEdit(UpdateView):
    model = models.Recipe
    fields = '__all__'
    template_name = 'edit.html'
    success_url = reverse_lazy('recipes')


class RecipeDelete(DeleteView):
    model = models.Recipe
    template_name = 'delete.html'
    success_url = reverse_lazy('recipes')
