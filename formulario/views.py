from django.shortcuts import render
from django.shortcuts import render

# Create your views here.

def formulario(request, *args, **kwargs):
    return render(request, "formulario.html", {})
