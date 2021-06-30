from django.shortcuts import render
from django.shortcuts import render

# Create your views here.

def consejos(request, *args, **kwargs):
    return render(request, "consejos.html", {})
def depresion(request, *args, **kwargs):
    return render(request, "depresion.html", {})