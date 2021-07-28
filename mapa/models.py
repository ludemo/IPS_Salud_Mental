from django.db import models

# Create your models here.

Centros = (
	(1, 'Hospital Honorio Delgado'),
	(2, 'Hospital Goyeneche'),
	(3, 'Clinica de Neuropsiquiatria y Salud Mental San Rafael'),
	(4, 'Centro de Salud Mental Muñoz'),
	(5, 'Centro de Salud Mental Comunitario Hunter'),
	(6, 'El Instituto de Salud Mental Carlos Alberto Seguin Escobedo'),
	(7, 'Centro de Adicciones Y Salud Mental'),
	(8, 'Centro de salud mental comunitario San Martin de Porres Arequipa'),
	(9, 'Clinica de Salud Mental y Adicciones'),
	(10, 'Centro Psicologico Kid Zone'),
	(11, 'Centro de Salud Mental y Adicciones Victor Raul Hinojosa'),
	(12, 'Centro de Salud Mental Comunitario CAYMA'),
	(13, 'Psicologos Bienestar - Sede Arequipa'),
	(14, 'Centro de Salud Mental Comunitario Simon Bolivar'),
	(15, 'Centro Psicologico de la Fuente'),
	(16, 'Centro Psicologico'),
	(17, 'Psicomedic-Tratamiento Psiquiatricos'),
	(18, 'Centro Psicologico - NEURO TALENTO'),
)
class Comentarios(models.Model):

	ComCod = models.AutoField(primary_key=True)
	nombreUser = models.CharField(max_length=100)
	comentario = models.CharField(max_length=300)
	centroAt = models.IntegerField(null=False, blank=False, choices=Centros)

	class Meta:
		verbose_name_plural = "Comentarios"