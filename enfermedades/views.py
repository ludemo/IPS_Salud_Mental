from django.shortcuts import render
from django.views.generic import TemplateView

from django.http import JsonResponse

from .models import Consejos




# Create your views here.
#Views basadas en función para renderizar los transtornos de salud mental

class Consejo(TemplateView):
    template_name = 'consejos.html'

    def get(self, request, *args, **kwargs):
        data = Consejos.objects.all()

        return JsonResponse(data)



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
