from ..models import ExperimentFile, ExperimentData
from ..models.ExperimentData import parse_and_save_data
from ..serializers import ExperimentFileSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist


class ExperimentFileViewSet(viewsets.ModelViewSet):
    queryset = ExperimentFile.objects.all()
    serializer_class = ExperimentFileSerializer

    @action(detail=True, methods=['get'])
    def parse_data(self, request, pk=None):
        experiment_file: ExperimentFile = self.get_object()
        try:
            ExperimentData.objects.get(experiment_file=experiment_file)
            return Response('Data already parsed', status=status.HTTP_403_FORBIDDEN)
        except ObjectDoesNotExist:
            parse_and_save_data(experiment_file)
            return Response('Data have been parsed', status=status.HTTP_200_OK)