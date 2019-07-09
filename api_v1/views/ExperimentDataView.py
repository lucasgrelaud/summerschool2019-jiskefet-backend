from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser

from ..models import ExperimentData
from ..serializers import ExperimentDataSerializer

@csrf_exempt
def experiment_data_list(request):
    """
    List all the experiments registered on the database
    """
    if request.method == 'GET':
        experiment_data = ExperimentData.objects.all()
        serializer = ExperimentDataSerializer(experiment_data, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ExperimentData(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def experiment_data_detail(request, pk):
    """
    Retrieve, update or delete a code experiment_data.
    """
    try:
        experiment_data = ExperimentData.objects.get(pk=pk)
    except ExperimentData.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = ExperimentDataSerializer(experiment_data)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ExperimentDataSerializer(experiment_data, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        experiment_data.delete()
        return HttpResponse(status=204)
