from django.db import models

# Create your models here.

class Consejos(models.Model):
    #Titulo del consejo
    conTit = models.CharField(max_length=40)
    #Descripcion del consejo
    conDes = models.TextField()
    #Url de la imagen
    conImaUrl = models.TextField()
