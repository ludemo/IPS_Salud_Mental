from django.forms import *
from .models import *
Centros = [
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
]
class ComentarioForm(ModelForm):
    
    class Meta:
        model = Comentarios
        fields = ('__all__')

        widgets = {
            'centroAt' : Select(           
                attrs={
                    'class':'comentarios__select'
                },
                
            ),
            'comentario' : TextInput(
                attrs={
                    'placeholder':'Escribe tu comentario',
                    'style':'border:none; background-color: transparent;',
                    'autocomplete':'off',
                    "class":"comentarios_text-input"
                }
            ),

            'nombreUser' : TextInput(
                attrs={
                    'style':'display:none',
                    
                }
            )
        }