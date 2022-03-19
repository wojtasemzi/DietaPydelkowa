from django.urls import path

from prices import views

urlpatterns = [
    # region Price
    path('', views.Prices.as_view(), name='prices'),

    path('add/', views.PriceAdd.as_view(), name='price_add'),
    path('<int:pk>/', views.Price.as_view(), name='price'),
    path('<int:pk>/edit/', views.PriceEdit.as_view(), name='price_edit'),
    path('<int:pk>/delete/', views.PriceDelete.as_view(), name='price_delete'),
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