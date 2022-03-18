from django import forms

from meals import models

class MealAdd(forms.ModelForm):
    class Meta:
        model = models.Meal
        fields = '__all__'