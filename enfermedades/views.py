from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from django.http import JsonResponse

from .models import Consejos, Enfermedad




# Create your views here.
#Views basadas en función para renderizar los transtornos de salud mental

class ConsejoView(ListView):
    template_name = 'consejos.html'
    model = Consejos

class EnfermedadDetailView(DetailView):
    template_name = "enfermedades.html"
    model = Enfermedad
    def get_context_data(self, **kwargs):
        context = super(EnfermedadDetailView,self).get_context_data(**kwargs)
        context['enfermedades_lista'] = Enfermedad.objects.all()
        return context
    


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


