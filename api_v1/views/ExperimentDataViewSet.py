from ..models import ExperimentData
from ..serializers import ExperimentDataSerializer
from rest_framework import viewsets


class ExperimentDataViewSet(viewsets.ModelViewSet):
    queryset = ExperimentData.objects.all()
    serializer_class = ExperimentDataSerializer
