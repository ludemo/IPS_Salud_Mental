from django.http import HttpResponse
from django.shortcuts import render
from enfermedades.models import Enfermedad

# Create your views here.
# View basada en función para renderizar el homepage
def home(request, *args, **kwargs):
    enfermedades = Enfermedad.objects.all()
    return render(request, "homepage.html", {'enfermedades': enfermedades})
