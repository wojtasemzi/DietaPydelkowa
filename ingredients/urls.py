from django.urls import path

from ingredients import views

urlpatterns = [
    path('', views.Ingredients.as_view(), name='ingredients'),

    path('add/', views.IngredientAdd.as_view(), name='ingredient_add'),
    path('<int:pk>/', views.Ingredient.as_view(), name='ingredient'),
    path('<int:pk>/edit/', views.IngredientEdit.as_view(), name='ingredient_edit'),
    path('<int:pk>/delete/', views.IngredientDelete.as_view(), name='ingredient_delete'),

    path('vitamin/', views.Vitamins.as_view(), name='vitamins'),

    path('vitamin/add/', views.VitaminAdd.as_view(), name='vitamin_add'),
    path('vitamin/<int:pk>/', views.Vitamin.as_view(), name='vitamin'),
    path('vitamin/<int:pk>/edit/', views.VitaminEdit.as_view(), name='vitamin_edit'),

]