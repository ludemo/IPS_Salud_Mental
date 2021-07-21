from django.http import HttpResponse
from django.shortcuts import render
from enfermedades.models import Enfermedad, PersonalM
from django.views.generic import TemplateView

# Create your views here.
# View basada en función para renderizar el homepage
class HomeView(TemplateView):
    template_name = "homepage.html"
    context_object_name = 'enfermedades'
    #enfermedades = Enfermedad.objects.all() 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['enfermedades'] = Enfermedad.objects.all()
        context['personalM'] = PersonalM.objects.all()
        return context
    

