from django.db import models
from .ExperimentFile import ExperimentFile
import datetime

METHOD_CHOICE = sorted([''])


# The parsed data of a BookKeeping Entry file
class ExperimentData(models.Model):
    experiment_file = models.ForeignKey(ExperimentFile, on_delete=models.CASCADE, default=-1)
    parsing_datetime = models.DateTimeField(auto_now=True)  # Datetime of when the file have been parsed
    parsing_method = models.CharField(max_length=50, default='', blank=False)  # The parsing method used to process the file content
    data = models.TextField(choices=METHOD_CHOICE, default='', blank=False)

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
        return '[' + self.parsing_method + "; " + self.parsing_datetime.strftime("%Y %m %d") + "]\n\"" + self.data \
               + "\""