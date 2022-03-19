from django import forms

from prices import models


class PriceAdd(forms.ModelForm):
    class Meta:
        model = models.Price
        fields = '__all__'


class CurrencyAdd(forms.ModelForm):
    class Meta:
        model = models.Currency
        fields = '__all__'


class UnitAdd(forms.ModelForm):
    class Meta:
        model = models.Unit
        fields = '__all__'


class StoreAdd(forms.ModelForm):
    class Meta:
        model = models.Store
        fields = '__all__'