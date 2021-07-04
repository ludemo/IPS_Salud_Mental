from django import forms
from .models import Pregunta
from django.forms import ModelForm
class AddForm(forms.ModelForm):
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
# Answer = (
#     (0, 'No'),
#     (1, 'Si'),
# )

# class Pregunta(models.Model):
#     ForCod = models.AutoField(primary_key=True)
#     #Pregunta = models.IntegerField(default=0)
#     Resp1 = forms.IntegerField(choices=Answer)
#     Resp2 = forms.IntegerField(choices=Answer)
#     Resp3 = forms.IntegerField(choices=Answer)
#     Resp4 = forms.IntegerField(choices=Answer)
#     Resp5 = forms.IntegerField(choices=Answer)
#     Resp6 = forms.IntegerField(choices=Answer)
#     Resp7 = forms.IntegerField(choices=Answer)
#     Resp8 = forms.IntegerField(choices=Answer)
#     Resp9 = forms.IntegerField(choices=Answer)
#     Resp10 = forms.IntegerField(choices=Answer)
#     Resp11 = forms.IntegerField(choices=Answer)
#     Resp12 = forms.IntegerField(choices=Answer)
#     Resp13 = forms.IntegerField(choices=Answer)
#     Resp14 = forms.IntegerField(choices=Answer)
#     Resp15 = forms.IntegerField(choices=Answer)
#     Resp16 = forms.IntegerField(choices=Answer)
#     Resp17 = forms.IntegerField(choices=Answer)
#     Resp18 = forms.IntegerField(choices=Answer)
#     Resp19 = forms.IntegerField(choices=Answer)