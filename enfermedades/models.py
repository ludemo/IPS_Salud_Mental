from django.db import models
from django.core.validators import MinLengthValidator
# Create your models here.

class Enfermedad(models.Model):

	nombreE = models.CharField(max_length=150)
	#imagenEF = models.ImageField(upload_to='img/enfermedades')
	descripcionE = models.TextField()
	sintoma1 = models.TextField(max_length=150, validators=[MinLengthValidator(15)])
	sintoma2 = models.TextField(max_length=150, validators=[MinLengthValidator(15)])
	sintoma3 = models.TextField(max_length=150, validators=[MinLengthValidator(15)])
	sintoma4 = models.TextField(max_length=150, validators=[MinLengthValidator(15)])
	imagenET = models.ImageField(upload_to='img/enfermedades')
	imagenSIN = models.ImageField(upload_to='img/enfermedades/sintomas', default='img/enfermedades/cerebro_duDVBew.png')

	class Meta:
		verbose_name_plural = "Enfermedades"
class PersonalM(models.Model):

	nombreP = models.CharField(max_length=200)
	especialidadP = models.CharField(max_length=100, default= ' ')
	imagenP = models.ImageField(upload_to='img/doctores')
	centroP = models.CharField(max_length=200)
	celularP = models.IntegerField()
	horarioP = models.CharField(max_length=100, default = ' ')

	class Meta:
		verbose_name_plural = "Personal Medico"

class Consejos(models.Model):
    #Titulo del consejo
    conTit = models.CharField(max_length=40)
    #Descripcion del consejo
    conDes = models.TextField(max_length=200, validators=[MinLengthValidator(15)])
    #Url de la imagen
    conImaUrl = models.TextField()

    class Meta:
    	verbose_name_plural = "Consejos"
