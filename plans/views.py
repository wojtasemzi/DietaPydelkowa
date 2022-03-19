from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import UpdateView

from plans import models
from plans import forms


# region Plan
class Plans(ListView):
    model = models.Plan
    context_object_name = 'objects'
    template_name = 'list.html'


class PlanAdd(CreateView):
    model = models.Plan
    form_class = forms.PlanAdd
    template_name = 'add.html'
    success_url = reverse_lazy('plans')


class Plan(DetailView):
    model = models.Plan
    template_name = 'object.html'


class PlanEdit(UpdateView):
    model = models.Plan
    fields = '__all__'
    template_name = 'edit.html'
    success_url = reverse_lazy('plans')


class PlanDelete(DeleteView):
    model = models.Plan
    template_name = 'delete.html'
    success_url = reverse_lazy('plans')
# endregion

# region Day

# endregion
