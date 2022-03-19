from django import forms

from plans import models

class PlanAdd(forms.ModelForm):
    class Meta:
        model = models.Plan
        fields = '__all__'


class DayAdd(forms.ModelForm):
    class Meta:
        model = models.Day
        fields = '__all__'
