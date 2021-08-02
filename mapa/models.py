from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

Centros = (
	('Hospital Honorio Delgado', 'Hospital Honorio Delgado'),
	('Hospital Goyeneche', 'Hospital Goyeneche'),
	('Clinica de Neuropsiquiatria y Salud Mental San Rafael', 'Clinica de Neuropsiquiatria y Salud Mental San Rafael'),
	('Centro de Salud Mental Muñoz', 'Centro de Salud Mental Muñoz'),
	('Centro de Salud Mental Comunitario Hunter', 'Centro de Salud Mental Comunitario Hunter'),
	('El Instituto de Salud Mental Carlos Alberto Seguin Escobedo', 'El Instituto de Salud Mental Carlos Alberto Seguin Escobedo'),
	('Centro de Adicciones Y Salud Mental', 'Centro de Adicciones Y Salud Mental'),
	('Centro de salud mental comunitario San Martin de Porres Arequipa', 'Centro de salud mental comunitario San Martin de Porres Arequipa'),
	('Clinica de Salud Mental y Adicciones', 'Clinica de Salud Mental y Adicciones'),
	('Centro Psicologico Kid Zone', 'Centro Psicologico Kid Zone'),
	('Centro de Salud Mental y Adicciones Victor Raul Hinojosa', 'Centro de Salud Mental y Adicciones Victor Raul Hinojosa'),
	('Centro de Salud Mental Comunitario CAYMA', 'Centro de Salud Mental Comunitario CAYMA'),
	('Psicologos Bienestar - Sede Arequipa', 'Psicologos Bienestar - Sede Arequipa'),
	('Centro de Salud Mental Comunitario Simon Bolivar', 'Centro de Salud Mental Comunitario Simon Bolivar'),
	('Centro Psicologico de la Fuente', 'Centro Psicologico de la Fuente'),
	('Centro Psicologico', 'Centro Psicologico'),
	('Psicomedic-Tratamiento Psiquiatricos', 'Psicomedic-Tratamiento Psiquiatricos'),
	('Centro Psicologico - NEURO TALENTO', 'Centro Psicologico - NEURO TALENTO'),
)

class Comentarios(models.Model):

	ComCod = models.AutoField(primary_key=True)
	nombreUser = models.CharField(max_length=100)
	comentario = models.TextField(max_length=200, validators=[MinLengthValidator(15)])
	centroAt = models.CharField(max_length=100, null=False, blank=False, choices=Centros)

	class Meta:
		verbose_name_plural = "Comentarios"