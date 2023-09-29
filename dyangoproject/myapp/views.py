from django.http import HttpResponse, JsonResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render

# Create your views here.

def index (request):
    title = "Titulo desde el render"
    
    return render(request, "index.html", {
        'title' : title
    })


def hello(request):
    return HttpResponse("Hola mundo")

def otraFuncion (request):
    return HttpResponse("Ahora le estoy respondiendo desde otra funcion")

def parametros (request, username):
    return HttpResponse("Este es el username: " + username)

def projects (request):
    projects = list(Project.objects.values())
    return JsonResponse(projects, safe=False)

def project (request, id):
    # project = Project.objects.get(id=id)
    p = get_object_or_404(Project, id=id)
    return HttpResponse(p.name)