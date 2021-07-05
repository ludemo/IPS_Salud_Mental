from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
# View basada en función para renderizar el homepage
def home(request, *args, **kwargs):
    return render(request, "homepage.html", {})
