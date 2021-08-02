from django.shortcuts import render, get_object_or_404, redirect
from .models import Preguntas
from django.views.generic import TemplateView

# Create your views here.  

class FormularioView(TemplateView):
	template_name = "formulario.html"
    #enfermedades = Enfermedad.objects.all() 


	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["preguntas"] = Preguntas.objects.all()
		return context







#View basada en función para renderizar formulario html (Inactiva)
def formulario(request, *args, **kwargs):
    return render(request, "formulario.html", {})

#View basada en función para validar a una llamada del form (Inactiva)
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

#View basada en función para responder a una llamada del form  y redigir (Inactiva)
def enviar(request, pk):
	if request.method == "POST":
		form = Formulario(request.POST)
	if form.is_valid():
		resp = form.cleaned_data["resp"]
		resp_final = dict(form.fields["resp_final"].choices)[resp_final]
		#form.save()
		return redirect('../../../.../')


