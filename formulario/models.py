from django.db import models
from django import forms
from django.forms import ModelForm

# Create your models here.

# class Formulario(models.Model):
#     ForCod = models.AutoField(primary_key=True)
#     ForUserId = models.IntegerField(default=0)

# class Respuesta(models.Model):
#     RepCod = models.AutoField(primary_key=True)
#     RepForCod = models.ForeignKey('Formulario', on_delete=models.CASCADE)
#     RepPreCod = models.ForeignKey('Pregunta', on_delete=models.CASCADE)
#     RepSiNoCod = models.ForeignKey('SiNo', on_delete=models.CASCADE)

# class Pregunta(models.Model):
#     PreCod = models.AutoField(primary_key=True)
#     PreDes = models.CharField(max_length=110)

# class SiNo(models.Model):
#     SiNoCod = models.AutoField(primary_key=True)
#     SiNoDes = models.CharField(max_length=2)
#  
Answer = (
    (0, 'No'),
    (1, 'Si'),
)

class Pregunta(models.Model):
    ForCod = models.AutoField(primary_key=True)
    #Pregunta = models.IntegerField(default=0)
    Resp1 = models.IntegerField(choices=Answer)
    Resp2 = models.IntegerField(choices=Answer)
    Resp3 = models.IntegerField(choices=Answer)
    Resp4 = models.IntegerField(choices=Answer)
    Resp5 = models.IntegerField(choices=Answer)
    Resp6 = models.IntegerField(choices=Answer)
    Resp7 = models.IntegerField(choices=Answer)
    Resp8 = models.IntegerField(choices=Answer)
    Resp9 = models.IntegerField(choices=Answer)
    Resp10 = models.IntegerField(choices=Answer)
    Resp11 = models.IntegerField(choices=Answer)
    Resp12 = models.IntegerField(choices=Answer)
    Resp13 = models.IntegerField(choices=Answer)
    Resp14 = models.IntegerField(choices=Answer)
    Resp15 = models.IntegerField(choices=Answer)
    Resp16 = models.IntegerField(choices=Answer)
    Resp17 = models.IntegerField(choices=Answer)
    Resp18 = models.IntegerField(choices=Answer)
    Resp19 = models.IntegerField(choices=Answer)

    def __str__(self):
        return self.name

class PreguntaForm(ModelForm):
    class Meta:
        model = Pregunta
        fields = [
            'ForCod',
            'Resp1',
            'Resp2',
            'Resp3',
            'Resp4',
            'Resp5',
            'Resp6',
            'Resp7',
            'Resp8',
            'Resp9',
            'Resp10',
            'Resp11',
            'Resp12',
            'Resp13',
            'Resp14',
            'Resp15',
            'Resp16',
            'Resp17',
            'Resp18',
            'Resp19',           
        ]