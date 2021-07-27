from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class MapaView(TemplateView):
    template_name = "mapa.html" 
