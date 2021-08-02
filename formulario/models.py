from django.db import models
from django.forms import ModelForm
from django.core.validators import MinLengthValidator


class Preguntas(models.Model):
    ForCod = models.AutoField(primary_key=True)
    pregunta = models.CharField(default= '',max_length=120, validators=[MinLengthValidator(15)])



