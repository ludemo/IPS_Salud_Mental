from django.db import models

# Create your models here.

class Enfermedad(models.Model):

	nombreE = models.CharField(max_length=200)
	#imagenEF = models.ImageField(upload_to='img/enfermedades')
	descripcionE = models.TextField()
	sintoma1 = models.TextField(default=' ')
	sintoma2 = models.TextField(default=' ')
	sintoma3 = models.TextField(default=' ')
	sintoma4 = models.TextField(default=' ')
	imagenET = models.ImageField(upload_to='img/enfermedades')
	imagenSIN = models.ImageField(upload_to='img/enfermedades/sintomas', default='img/enfermedades/cerebro_duDVBew.png')

	class Meta:
		verbose_name_plural = "Enfermedades"
class PersonalM(models.Model):

	nombreP = models.CharField(max_length=200)
	imagenP = models.ImageField(upload_to='img/doctores')
	centroP = models.CharField(max_length=200)
	celularP = models.IntegerField()

	class Meta:
		verbose_name_plural = "Personal Medico"

class Consejos(models.Model):
    #Titulo del consejo
    conTit = models.CharField(max_length=40)
    #Descripcion del consejo
    conDes = models.TextField()
    #Url de la imagen
    conImaUrl = models.TextField()

    class Meta:
    	verbose_name_plural = "Consejos"
