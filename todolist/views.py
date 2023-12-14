from django.http import JsonResponse


# Create your views here.
def index(request):
    data = [1, 2, 3, 4, 5]

    return JsonResponse(data, safe=False, status=400)
