from django.shortcuts import render, get_object_or_404, redirect
from .models import Pregunta
from .form import AddForm 

# Create your views here.  

def formulario(request, *args, **kwargs):
    return render(request, "formulario.html", {})

def enviarForm(request, myID):
	obj = Pregunta.objects.get(id = myID)
	form = AddForm(request.POST or None, instance = obj)
	
	if form.is_valid():
		form.save()
		form = AddForm()
		return redirect('../../../')

	context = {
		'form': form,
	}
	return render(request, "formulario.html", context)