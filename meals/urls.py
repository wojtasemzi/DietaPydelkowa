from django.urls import path

from meals import views

urlpatterns = [
    path('', views.Meals.as_view(), name='meals'),

    path('add/', views.MealAdd.as_view(), name='meal_add'),
    path('<int:pk>/', views.Meal.as_view(), name='meal'),
    path('<int:pk>/edit/', views.MealEdit.as_view(), name='meal_edit'),
    path('<int:pk>/delete/', views.MealDelete.as_view(), name='meal_delete'),
]