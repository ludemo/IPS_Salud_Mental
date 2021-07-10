from django.db import models

# Create your models here.

class Enfermedad(models.Model):

	nombreE = models.CharField(max_length=200)
	imagenEF = models.ImageField(upload_to='img/enfermedades')
	descripcionE = models.TextField(max_length=200)
	estrategia = models.TextField()
	imagenET = models.ImageField(upload_to='img/enfermedades')
