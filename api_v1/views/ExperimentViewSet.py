from ..models import Experiment
from ..serializers import ExperimentSerializer
from rest_framework import viewsets


class ExperimentViewSet(viewsets.ModelViewSet):
    queryset = Experiment.objects.all()
    serializer_class = ExperimentSerializer
