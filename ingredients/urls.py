from django.urls import path

from ingredients import views

urlpatterns = [
    # region Ingridient
    path('', views.Ingredients.as_view(), name='ingredients'),

    path('add/', views.IngredientAdd.as_view(), name='ingredient_add'),
    path('<int:pk>/', views.Ingredient.as_view(), name='ingredient'),
    path('<int:pk>/edit/', views.IngredientEdit.as_view(), name='ingredient_edit'),
    path('<int:pk>/delete/', views.IngredientDelete.as_view(), name='ingredient_delete'),
    # endregion
    # region Vitamin
    path('vitamin/', views.Vitamins.as_view(), name='vitamins'),

    path('vitamin/add/', views.VitaminAdd.as_view(), name='vitamin_add'),
    path('vitamin/<int:pk>/', views.Vitamin.as_view(), name='vitamin'),
    path('vitamin/<int:pk>/edit/', views.VitaminEdit.as_view(), name='vitamin_edit'),
    path('vitamin/<int:pk>/delete/', views.VitaminDelete.as_view(), name='vitamin_delete'),
    # endregion
    # region Minerals
    path('mineral/', views.Minerals.as_view(), name='minerals'),

    path('mineral/add/', views.MineralAdd.as_view(), name='mineral_add'),
    path('mineral/<int:pk>/', views.Mineral.as_view(), name='mineral'),
    path('mineral/<int:pk>/edit/', views.MineralEdit.as_view(), name='mineral_edit'),
    path('mineral/<int:pk>/delete/', views.MineralDelete.as_view(), name='mineral_delete'),
    # endregion
]