from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class EstadisticasView(TemplateView):
    template_name = "estadisticas.html"
