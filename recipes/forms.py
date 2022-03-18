from django import forms

from recipes import models

class RecipeAdd(forms.ModelForm):
    class Meta:
        model = models.Recipe
        fields = '__all__'