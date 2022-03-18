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
    # region Mineral
    path('mineral/', views.Minerals.as_view(), name='minerals'),

    path('mineral/add/', views.MineralAdd.as_view(), name='mineral_add'),
    path('mineral/<int:pk>/', views.Mineral.as_view(), name='mineral'),
    path('mineral/<int:pk>/edit/', views.MineralEdit.as_view(), name='mineral_edit'),
    path('mineral/<int:pk>/delete/', views.MineralDelete.as_view(), name='mineral_delete'),
    # endregion
    # region Tag
    path('tag/', views.Tags.as_view(), name='tags'),

    path('tag/add/', views.TagAdd.as_view(), name='tag_add'),
    path('tag/<int:pk>/', views.Tag.as_view(), name='tag'),
    path('tag/<int:pk>/edit/', views.TagEdit.as_view(), name='tag_edit'),
    path('tag/<int:pk>/delete/', views.TagDelete.as_view(), name='tag_delete'),
    # endregion
    # region Price
    path('price/', views.Prices.as_view(), name='prices'),

    path('price/add/', views.PriceAdd.as_view(), name='price_add'),
    path('price/<int:pk>/', views.Price.as_view(), name='price'),
    path('price/<int:pk>/edit/', views.PriceEdit.as_view(), name='price_edit'),
    path('price/<int:pk>/delete/', views.PriceDelete.as_view(), name='price_delete'),
    # endregion
    # region Currency
    path('currency/', views.Currencys.as_view(), name='currencys'),

    path('currency/add/', views.CurrencyAdd.as_view(), name='currency_add'),
    path('currency/<int:pk>/', views.Currency.as_view(), name='currency'),
    path('currency/<int:pk>/edit/', views.CurrencyEdit.as_view(), name='currency_edit'),
    path('currency/<int:pk>/delete/', views.CurrencyDelete.as_view(), name='currency_delete'),
    # endregion
    # region Unit
    path('unit/', views.Units.as_view(), name='units'),

    path('unit/add/', views.UnitAdd.as_view(), name='unit_add'),
    path('unit/<int:pk>/', views.Unit.as_view(), name='unit'),
    path('unit/<int:pk>/edit/', views.UnitEdit.as_view(), name='unit_edit'),
    path('unit/<int:pk>/delete/', views.UnitDelete.as_view(), name='unit_delete'),
    # endregion
    # region Store
    path('store/', views.Stores.as_view(), name='stores'),

    path('store/add/', views.StoreAdd.as_view(), name='store_add'),
    path('store/<int:pk>/', views.Store.as_view(), name='store'),
    path('store/<int:pk>/edit/', views.StoreEdit.as_view(), name='store_edit'),
    path('store/<int:pk>/delete/', views.StoreDelete.as_view(), name='store_delete'),
    # endregion
]
