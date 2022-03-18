from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from meals import forms
from meals import models


class Meals(ListView):
    model = models.Meal
    context_object_name = 'objects'
    template_name = 'list.html'


class MealAdd(CreateView):
    model = models.Meal
    form_class = forms.MealAdd
    template_name = 'add.html'
    success_url = reverse_lazy('meals')


class Meal(DetailView):
    model = models.Meal
    template_name = 'object.html'


class MealEdit(UpdateView):
    model = models.Meal
    fields = '__all__'
    template_name = 'edit.html'
    success_url = reverse_lazy('meals')


class MealDelete(DeleteView):
    model = models.Meal
    template_name = 'delete.html'
    success_url = reverse_lazy('meals')
