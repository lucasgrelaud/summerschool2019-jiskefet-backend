from django.db import models
from api_v1.models.Experiment import Experiment
import datetime


# A BookKeeping Entry for an experiment
class ExperimentFile(models.Model):
    experiment = models.ForeignKey(Experiment, default=-1, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default='', blank=False)  # Title given to the experiment BookKeeping Entry
    file_name = models.CharField(default='', max_length=200, blank=False)
    file_mime = models.CharField(default='', max_length=100, blank=False)
    file_content = models.TextField(default='', blank=False)

    def get_experiment_id(self) -> Experiment:
        return self.experiment

    def get_title(self) -> str:
        return self.title

    def get_file_name(self) -> str:
        return self.file_name

    def get_file_mime(self) -> str:
        return self.file_mime

    def get_file_content(self) -> str:
        return self.file_content

    def set_experiment(self, experiment: Experiment):
        self.experiment = experiment

    def set_title(self, title: str) -> None:
        self.title = title

    def set_file_name(self, file_name: str) -> None:
        self.file_name = file_name

    def set_file_mime(self, file_mime: str) -> None:
        self.file_mime = file_mime

    def set_file_content(self, file_content: str) -> None:
        self.file_content = file_content

    def __str__(self):
        return self.title + ":\n[" + self.file_name + "; " + self.file_mime + "]"

