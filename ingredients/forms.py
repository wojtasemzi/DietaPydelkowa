from django import forms

from ingredients import models


class IngredientAdd(forms.ModelForm):
    class Meta:
        model = models.Ingredient
        fields = '__all__'
