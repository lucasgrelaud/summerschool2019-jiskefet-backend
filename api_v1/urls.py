from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('experiments/', views.experiment_list),
    path('experiments/<int:pk>/', views.experiment_detail)
]