from django.shortcuts import render, get_object_or_404, redirect
from .models import Formulario
from .form import Formulario 

# Create your views here.  

def formulario(request, *args, **kwargs):
    return render(request, "formulario.html", {})

def enviarForm(request, myID):
	obj = Formulario.objects.get(id = myID)
	form = Formulario(request.POST or None, instance = obj)
	
	if form.is_valid():
		form.save()
		form = AddForm()
		return redirect('../../../')

	context = {
		'form': form,
	}
	return render(request, "formulario.html", context)


def enviar(request, pk):
	if request.method == "POST":
		form = Formulario(request.POST)
	if form.is_valid():
		resp = form.cleaned_data["resp"]
		resp_final = dict(form.fields["resp_final"].choices)[resp_final]
		#form.save()
		return redirect('../../../.../')
