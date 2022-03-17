from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView
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


class Ingredient(DetailView):
    model = models.Ingredient
    template_name = 'object.html'


class IngredientEdit(UpdateView):
    model = models.Ingredient
    fields = '__all__'
    template_name = 'add.html'
    success_url = reverse_lazy('ingredients')


class IngredientDelete(DeleteView):
    model = models.Ingredient
    template_name = 'delete.html'
    success_url = reverse_lazy('ingredients')


class Vitamins(ListView):
    model = models.Vitamin
    context_object_name = 'objects'
    template_name = 'list.html'


class VitaminAdd(CreateView):
    model = models.Vitamin
    form_class = forms.VitaminAdd
    template_name = 'add.html'
    success_url = reverse_lazy('vitamins')


class Vitamin(DetailView):
    model = models.Vitamin
    template_name = 'object.html'


class VitaminEdit(UpdateView):
    model = models.Vitamin
    fields = '__all__'
    template_name = 'edit.html'
    success_url = reverse_lazy('vitamins')


class VitaminDelete(DeleteView):
    model = models.Vitamin
    template_name = 'delete.html'
    success_url = reverse_lazy('vitamins')
