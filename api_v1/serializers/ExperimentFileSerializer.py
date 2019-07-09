from rest_framework import serializers
from api_v1.models.ExperimentFile import ExperimentFile


class ExperimentFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperimentFile
        fields = ('experiment', 'title', 'file_name', 'file_mime', 'file_content')