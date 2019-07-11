from rest_framework import serializers
from ..models.ExperimentData import ExperimentData


class ExperimentDataSerializer(serializers.ModelSerializer):
    data = serializers.JSONField(binary=True)

    class Meta:
        model = ExperimentData
        fields = ('experiment_file', 'parsing_datetime', 'parsing_method', 'data')
