from django.db import models

# Create your models here.

class Formulario(models.Model):
    ForCod = models.AutoField(primary_key=True)
    ForUserId = models.IntegerField(default=0)

class Respuesta(models.Model):
    RepCod = models.AutoField(primary_key=True)
    RepForCod = models.ForeignKey('Formulario', on_delete=models.CASCADE)
    RepPreCod = models.ForeignKey('Pregunta', on_delete=models.CASCADE)
    RepSiNoCod = models.ForeignKey('SiNo', on_delete=models.CASCADE)

class Pregunta(models.Model):
    PreCod = models.AutoField(primary_key=True)
    PreDes = models.CharField(max_length=110)

class SiNo(models.Model):
    SiNoCod = models.AutoField(primary_key=True)
    SiNoDes = models.CharField(max_length=2)
