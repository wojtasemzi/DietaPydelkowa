from django.shortcuts import render

from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from prices import models
from prices import forms

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


# region Unit
class Units(ListView):
    model = models.Unit
    context_object_name = 'objects'
    template_name = 'list.html'


class UnitAdd(CreateView):
    model = models.Unit
    form_class = forms.UnitAdd
    template_name = 'add.html'
    success_url = reverse_lazy('units')


class Unit(DetailView):
    model = models.Unit
    template_name = 'object.html'


class UnitEdit(UpdateView):
    model = models.Unit
    fields = '__all__'
    template_name = 'edit.html'
    success_url = reverse_lazy('units')


class UnitDelete(DeleteView):
    model = models.Unit
    template_name = 'delete.html'
    success_url = reverse_lazy('units')
# endregion


# region Store
class Stores(ListView):
    model = models.Store
    context_object_name = 'objects'
    template_name = 'list.html'


class StoreAdd(CreateView):
    model = models.Store
    form_class = forms.StoreAdd
    template_name = 'add.html'
    success_url = reverse_lazy('stores')


class Store(DetailView):
    model = models.Store
    template_name = 'object.html'


class StoreEdit(UpdateView):
    model = models.Store
    fields = '__all__'
    template_name = 'edit.html'
    success_url = reverse_lazy('stores')


class StoreDelete(DeleteView):
    model = models.Store
    template_name = 'delete.html'
    success_url = reverse_lazy('stores')
# endregion

