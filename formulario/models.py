from django.db import models
from django import forms
from django.forms import ModelForm
 

class Formulario(models.Model):
    Answer = (
        (0, 'No'),
        (1, 'Si'),
    )

    ForCod = models.AutoField(primary_key=True)
    #Pregunta = models.IntegerField(default=0)
    Resp1 = models.CharField(max_length=2, choices=Answer)
    Resp2 = models.CharField(max_length=2, choices=Answer)
    Resp3 = models.CharField(max_length=2, choices=Answer)
    Resp4 = models.CharField(max_length=2, choices=Answer)
    Resp5 = models.CharField(max_length=2, choices=Answer)
    Resp6 = models.CharField(max_length=2, choices=Answer)
    Resp7 = models.CharField(max_length=2, choices=Answer)
    Resp8 = models.CharField(max_length=2, choices=Answer)
    Resp9 = models.CharField(max_length=2, choices=Answer)
    Resp10 = models.CharField(max_length=2, choices=Answer)
    Resp11 = models.CharField(max_length=2, choices=Answer)
    Resp12 = models.CharField(max_length=2, choices=Answer)
    Resp13 = models.CharField(max_length=2, choices=Answer)
    Resp14 = models.CharField(max_length=2, choices=Answer)
    Resp15 = models.CharField(max_length=2, choices=Answer)
    Resp16 = models.CharField(max_length=2, choices=Answer)
    Resp17 = models.CharField(max_length=2, choices=Answer)
    Resp18 = models.CharField(max_length=2, choices=Answer)
    Resp19 = models.CharField(max_length=2, choices=Answer)

    def __str__(self):
        return self.name








# class PreguntaForm(ModelForm):
#     class Meta:
#         model = Pregunta
#         fields = [
#             'ForCod',
#             'Resp1',
#             'Resp2',
#             'Resp3',
#             'Resp4',
#             'Resp5',
#             'Resp6',
#             'Resp7',
#             'Resp8',
#             'Resp9',
#             'Resp10',
#             'Resp11',
#             'Resp12',
#             'Resp13',
#             'Resp14',
#             'Resp15',
#             'Resp16',
#             'Resp17',
#             'Resp18',
#             'Resp19',           
#         ]