from django.http import HttpResponse


def index(request):
    return HttpResponse("The API V1 is Working")