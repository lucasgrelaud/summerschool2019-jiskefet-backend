from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from api_v1.models import ExperimentFile
from api_v1.serializers import ExperimentFileSerializer

@csrf_exempt
def experiment_file_list(request):
    """
    List all the experiments registered on the database
    """
    if request.method == 'GET':
        experiment = ExperimentFile.objects.all()
        serializer = ExperimentFileSerializer(experiment, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ExperimentFile(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def experiment_file_detail(request, pk):
    """
    Retrieve, update or delete a code experiment.
    """
    try:
        experiment = ExperimentFile.objects.get(pk=pk)
    except ExperimentFile.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ExperimentFileSerializer(experiment)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ExperimentFileSerializer(experiment, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        experiment.delete()
        return HttpResponse(status=204)
