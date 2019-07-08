from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from api_v1.models import Experiment
from api_v1.serializers import ExperimentSerializer


def index(request):
    return HttpResponse("The API V1 is Working")


@csrf_exempt
def experiment_list(request):
    """
    List all the experiments registered on the database
    """
    if request.method == 'GET':
        experiment = Experiment.objects.all()
        serializer = ExperimentSerializer(experiment, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = Experiment(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def experiment_detail(request, pk):
    """
    Retrieve, update or delete a code experiment.
    """
    try:
        experiment = Experiment.objects.get(pk=pk)
    except Experiment.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ExperimentSerializer(experiment)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ExperimentSerializer(experiment, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        experiment.delete()
        return HttpResponse(status=204)
