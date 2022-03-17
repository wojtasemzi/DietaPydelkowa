from django.urls import path

from ingredients import views

urlpatterns = [
    path('', views.Ingredients.as_view(), name='ingredients'),
]