from rest_framework import serializers
from api_v1.models.Experiment import Experiment


class ExperimentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiment
        fields = ('name', 'description', 'start_date', 'end_date')