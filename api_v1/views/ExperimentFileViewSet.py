from ..models import ExperimentFile
from ..serializers import ExperimentFileSerializer
from rest_framework import viewsets


class ExperimentFileViewSet(viewsets.ModelViewSet):
    queryset = ExperimentFile.objects.all()
    serializer_class = ExperimentFileSerializer
