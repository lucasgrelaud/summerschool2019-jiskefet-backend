from django.db import models
import datetime


# A CERN experiment that need to be added to the BookKeeping platform
class Experiment(models.Model):
    name = models.CharField(max_length=100, default='', blank=False)
    description = models.TextField(blank=True)
    start_date = models.DateField(default='', blank=False)
    end_date = models.DateField(default='', blank=True)

    def get_name(self) -> str:
        return self.name

    def get_description(self) -> str:
        return self.description

    def get_start_date(self) -> datetime:
        return self.start_date

    def get_end_date(self) -> datetime:
        return self.end_date

    def set_name(self, name: str) -> None:
        self.name = name

    def set_start_date(self, start_date: datetime) -> None:
        self.start_date = start_date

    def set_end_date(self, end_date: datetime) -> None:
        self.end_date = end_date

    def set_description(self, description: str) -> None:
        self.description = description

    def __str__(self):
        return self.name + ":\n" + self.description + "\n[Start : " + self.start_date.strftime("%Y %m %d") + "; End :" \
               + self.end_date.strftime("%Y %m %d") + "]"

