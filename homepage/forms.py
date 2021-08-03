from django.forms import *
from .models import *

class ComentarioHForm(ModelForm):
    
    class Meta:
        model = ComentariosHome
        fields = ('__all__')

        widgets = {
            'comentarioH' : TextInput(
                attrs={
                    'placeholder':'Escribe tu comentario',
                    'autocomplete':'off',
                    'class':'comentarios_text-input'
                }
            ),
            'nombreUserH' : TextInput(
                attrs={
                    'style':'display:none',
                    
                }
            )
        }