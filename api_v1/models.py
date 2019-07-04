from django.db import models


# A CERN experiment that need to be added to the BookKeeping platform
class Experiment(models.Model):
    name = models.CharField(max_length=100, default='', blank=False)
    description = models.TextField(blank=True)
    start_date = models.DateField(null=True, blank=False)
    end_date = models.DateField(default=start_date, blank=True)


# A BookKeeping Entry for an experiment
class ExperimentFile(models.Model):
    experiment_id = models.ForeignKey(Experiment, default=-1, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default='', blank=False)  # Title given to the experiment BookKeeping Entry
    file_name = models.CharField(default='', max_length=200, blank=False)
    file_mime = models.CharField(default='', max_length=100, blank=False)
    file_content = models.TextField(default='', blank=False)


# The parsed data of a BookKeeping Entry file
class ExperimentData(models.Model):
    experiment_file_id = models.ForeignKey(ExperimentFile, on_delete=models.CASCADE, default=-1)
    parsing_datetime = models.DateTimeField(auto_now=True)  # Datetime of when the file have been parsed
    parsing_method = models.CharField(max_length=50, default='', blank=False)  # The parsing method used to process the file content
    data = models.TextField(default='', blank=False)

    # TODO : Add Feild.choice to the parsing_method field
