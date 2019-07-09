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
        experiment_file = ExperimentFile.objects.all()
        serializer = ExperimentFileSerializer(experiment_file, many=True)
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
    Retrieve, update or delete a code experiment_file.
    """
    try:
        experiment_file = ExperimentFile.objects.get(pk=pk)
    except ExperimentFile.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ExperimentFileSerializer(experiment_file)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ExperimentFileSerializer(experiment_file, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        experiment_file.delete()
        return HttpResponse(status=204)
