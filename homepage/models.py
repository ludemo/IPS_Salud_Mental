from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class ComentariosHome(models.Model):
    comHCod = models.AutoField(primary_key=True)
    nombreUserH = models.CharField(max_length=200)
    comentarioH = models.TextField(max_length=200,  validators=[MinLengthValidator(15)])

