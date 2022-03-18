from django import forms

from ingredients import models


class IngredientAdd(forms.ModelForm):
    class Meta:
        model = models.Ingredient
        fields = '__all__'


class VitaminAdd(forms.ModelForm):
    class Meta:
        model = models.Vitamin
        fields = '__all__'


class MineralAdd(forms.ModelForm):
    class Meta:
        model = models.Mineral
        fields = '__all__'


class TagAdd(forms.ModelForm):
    class Meta:
        model = models.Tag
        fields = '__all__'


class PriceAdd(forms.ModelForm):
    class Meta:
        model = models.Price
        fields = '__all__'
