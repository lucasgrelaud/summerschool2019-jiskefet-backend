from django.contrib import admin
from api_v1.models import Experiment, ExperimentFile, ExperimentData

admin.site.register(Experiment)
admin.site.register(ExperimentFile)
admin.site.register(ExperimentData)
# Register your models here.
