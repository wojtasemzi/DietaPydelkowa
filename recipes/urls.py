from django.urls import path

from recipes import views

urlpatterns = [
    path('', views.Recipes.as_view(), name='recipes'),

    path('add/', views.RecipeAdd.as_view(), name='recipe_add'),
    path('<int:pk>/', views.Recipe.as_view(), name='recipe'),
    path('<int:pk>/edit/', views.RecipeEdit.as_view(), name='recipe_edit'),
    path('<int:pk>/delete/', views.RecipeDelete.as_view(), name='recipe_delete'),
]
