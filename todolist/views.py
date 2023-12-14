from django.http import JsonResponse

from .models import Todo


# Create your views here.
def index(request):
    todos = Todo.objects.all()

    return JsonResponse(todos, safe=False, status=200)
