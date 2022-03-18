from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.shortcuts import render

from ingredients import forms
from ingredients import models


# region Ingredient
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
# endregion


# region Vitamin
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
# endregion


# region Mineral
class Minerals(ListView):
    model = models.Mineral
    context_object_name = 'objects'
    template_name = 'list.html'


class MineralAdd(CreateView):
    model = models.Mineral
    form_class = forms.MineralAdd
    template_name = 'add.html'
    success_url = reverse_lazy('minerals')


class Mineral(DetailView):
    model = models.Mineral
    template_name = 'object.html'


class MineralEdit(UpdateView):
    model = models.Mineral
    fields = '__all__'
    template_name = 'edit.html'
    success_url = reverse_lazy('minerals')


class MineralDelete(DeleteView):
    model = models.Mineral
    template_name = 'delete.html'
    success_url = reverse_lazy('minerals')
# endregion


# region Tag
class Tags(ListView):
    model = models.Tag
    context_object_name = 'objects'
    template_name = 'list.html'


class TagAdd(CreateView):
    model = models.Tag
    form_class = forms.TagAdd
    template_name = 'add.html'
    success_url = reverse_lazy('tags')


class Tag(DetailView):
    model = models.Tag
    template_name = 'object.html'


class TagEdit(UpdateView):
    model = models.Tag
    fields = '__all__'
    template_name = 'edit.html'
    success_url = reverse_lazy('tags')


class TagDelete(DeleteView):
    model = models.Tag
    template_name = 'delete.html'
    success_url = reverse_lazy('tags')
# endregion


# region Price
class Prices(ListView):
    model = models.Price
    context_object_name = 'objects'
    template_name = 'list.html'


class PriceAdd(CreateView):
    model = models.Price
    form_class = forms.PriceAdd
    template_name = 'add.html'
    success_url = reverse_lazy('prices')


class Price(DetailView):
    model = models.Price
    template_name = 'object.html'


class PriceEdit(UpdateView):
    model = models.Price
    fields = '__all__'
    template_name = 'edit.html'
    success_url = reverse_lazy('prices')


class PriceDelete(DeleteView):
    model = models.Price
    template_name = 'delete.html'
    success_url = reverse_lazy('prices')
# endregion


# region Currency
class Currencys(ListView):
    model = models.Currency
    context_object_name = 'objects'
    template_name = 'list.html'


class CurrencyAdd(CreateView):
    model = models.Currency
    form_class = forms.CurrencyAdd
    template_name = 'add.html'
    success_url = reverse_lazy('currencys')


class Currency(DetailView):
    model = models.Currency
    template_name = 'object.html'


class CurrencyEdit(UpdateView):
    model = models.Currency
    fields = '__all__'
    template_name = 'edit.html'
    success_url = reverse_lazy('currencys')


class CurrencyDelete(DeleteView):
    model = models.Currency
    template_name = 'delete.html'
    success_url = reverse_lazy('currencys')
# endregion
