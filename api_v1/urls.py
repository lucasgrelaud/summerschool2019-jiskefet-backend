from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'experiments', views.ExperimentViewSet)
router.register(r'file', views.ExperimentFileViewSet)
router.register(r'data', views.ExperimentDataViewSet)

urlpatterns = [
    path('', include(router.urls)),
]