import datetime
from django.db import models
from django.contrib.postgres.fields import JSONField
from .ExperimentFile import ExperimentFile

import base64
from io import StringIO
from xmljson import parker, Parker
from lxml.etree import parse, ElementTree
from json import dumps


METHOD_CHOICE = sorted([('XML', 'xml parser'), ('PLAIN', 'plaintext parser'), ('JSON', 'json parser')])


# The parsed data of a BookKeeping Entry file
class ExperimentData(models.Model):
    experiment_file = models.ForeignKey(ExperimentFile, on_delete=models.CASCADE, default=-1)
    parsing_datetime = models.DateTimeField(auto_now=True)  # Datetime of when the file have been parsed
    parsing_method = models.CharField(choices=METHOD_CHOICE, max_length=50, default='', blank=False)  # The parsing method used to process the file content
    data = JSONField(default=dict, blank=False)

    class Meta:
        ordering = ['-id']

    def get_experiment_file(self) -> ExperimentFile:
        return self.experiment_file

    def get_parsing_datetime(self) -> datetime:
        return self.parsing_datetime

    def get_parsing_method(self) -> str:
        return self.parsing_method

    def get_date(self) -> str:
        return self.data

    def set_parsing_datetime(self, parsing_datetime: datetime) -> None:
        self.parsing_datetime = parsing_datetime

    def set_parsing_method(self, parsing_method: str) -> None:
        self.parsing_method = parsing_method

    def set_date(self, data: str) -> None:
        self.data = data

    def __str__(self):
        return '[' + self.parsing_method + "; " + self.parsing_datetime.strftime("%Y %m %d") + "]\n"


def parse_and_save_data(experiement_file):
    experiment_data = ExperimentData()
    experiment_data.experiment_file = experiement_file
    if "xml" in experiment_data.experiment_file.get_file_mime():
        root = parse(StringIO(experiment_data.experiment_file.get_file_content()))
        experiment_data.data = dumps(parker.data(root.getroot()))
        experiment_data.parsing_method = 'XML'

    experiment_data.parsing_datetime = datetime.datetime.now()
    experiment_data.save()
