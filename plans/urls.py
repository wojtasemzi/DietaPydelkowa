from django.urls import path

from plans import views

urlpatterns = [
    path('', views.Plans.as_view(), name='plans'),

    path('add/', views.PlanAdd.as_view(), name='plan_add'),
    path('<int:pk>/', views.Plan.as_view(), name='plan'),
    path('<int:pk>/edit/', views.PlanEdit.as_view(), name='plan_edit'),
    path('<int:pk>/delete/', views.PlanDelete.as_view(), name='plan_delete'),
]