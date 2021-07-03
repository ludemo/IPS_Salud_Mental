from django.shortcuts import render
from django.shortcuts import render

# Create your views here.

def consejos(request, *args, **kwargs):
    return render(request, "consejos.html", {})
def depresion(request, *args, **kwargs):
    return render(request, "depresion.html", {})
def alcoholismo(request, *args, **kwargs):
    return render(request, "alcoholismo.html", {})
def ansiedad(request, *args, **kwargs):
    return render(request, "ansiedad.html", {})
def psicosis(request, *args, **kwargs):
    return render(request, "psicosis.html", {})
def violencia_familiar(request, *args, **kwargs):
    return render(request, "violencia_familiar.html", {})