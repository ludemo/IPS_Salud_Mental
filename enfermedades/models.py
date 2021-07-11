from django.db import models

# Create your models here.

<<<<<<< HEAD
class Enfermedad(models.Model):

	nombreE = models.CharField(max_length=200)
	imagenEF = models.ImageField(upload_to='img/enfermedades')
	descripcionE = models.TextField(max_length=200)
	estrategia = models.TextField()
	imagenET = models.ImageField(upload_to='img/enfermedades')
=======
class Consejos(models.Model):
    #Titulo del consejo
    conTit = models.CharField(max_length=40)
    #Descripcion del consejo
    conDes = models.TextField()
    #Url de la imagen
    conImaUrl = models.TextField()
>>>>>>> 3cdb5eb9ffd2a2ccb95d05ceefff9802409f8d88
