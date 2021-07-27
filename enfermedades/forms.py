from django import forms
from .models import PersonalM, Enfermedad

#####################################################
#personal medico
class AddForm(forms.ModelForm):
	class Meta:
		model = PersonalM
		fields = [
			'nombreP',
			'imagenp',
			'centroP',
			'celularP',
		]


class RawDestinationForm(forms.Form):
	nombreP = forms.CharField(max_length=200)
	imagenP = forms.ImageField(upload_to='img/doctores')
	centroP = forms.CharField(max_length=200)
	celularP = forms.IntegerField()


####################################################33
#enfermedad		
class AddForm(forms.ModelForm):
	class Meta:
		model = Enfermedad
		fields = [
			'nombreE',
			'imagenEF',
			'descripcionE',
			'estrategia',
			'imagenET',
		]


class RawEnfermedadForm(forms.Model):

	nombreE = forms.CharField(max_length=200)
	imagenEF = forms.ImageField(upload_to='img/enfermedades')
	descripcionE = forms.TextField(max_length=200)
	estrategia = forms.TextField()
	imagenET = forms.ImageField(upload_to='img/enfermedades')