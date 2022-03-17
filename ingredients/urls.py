from django.urls import path

from ingredients import views

urlpatterns = [
    path('', views.Ingredients.as_view(), name='ingredients'),

    path('add/', views.IngredientAdd.as_view(), name='ingredient_add'),
    path('<int:pk>/', views.Ingredient.as_view(), name='ingredient'),
]