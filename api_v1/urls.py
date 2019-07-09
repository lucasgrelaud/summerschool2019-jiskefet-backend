from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('experiments/', views.experiment_list),
    path('experiments/<int:pk>/', views.experiment_detail),
    path('file/', views.experiment_file_list),
    path('file/<int:pk>/', views.experiment_file_detail),
    path('data/', views.experiment_data_list),
    path('data/<int:pk>/', views.experiment_data_detail)
]