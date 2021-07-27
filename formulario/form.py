from django import forms
from .models import Formulario
from django.forms import ModelForm

class Formulario(forms.Form):
	Answer = (
    	(0, 'No'),
    	(1, 'Si'),
    )
    #ForCod = models.CharField(primary_key=True)
	ForCod = forms.IntegerField()
    #Pregunta = models.IntegerField(default=0)
	Resp1 = forms.ChoiceField(choices=Answer, widget=forms.RadioSelect())
	Resp2 = forms.ChoiceField(choices=Answer, widget=forms.RadioSelect())
	Resp3 = forms.ChoiceField(choices=Answer, widget=forms.RadioSelect())
	Resp4 = forms.ChoiceField(choices=Answer, widget=forms.RadioSelect())
	Resp5 = forms.ChoiceField(choices=Answer, widget=forms.RadioSelect())
	Resp6 = forms.ChoiceField(choices=Answer, widget=forms.RadioSelect())
	Resp7 = forms.ChoiceField(choices=Answer, widget=forms.RadioSelect())
	Resp8 = forms.ChoiceField(choices=Answer, widget=forms.RadioSelect())
	Resp9 = forms.ChoiceField(choices=Answer, widget=forms.RadioSelect())
	Resp10 = forms.ChoiceField(choices=Answer, widget=forms.RadioSelect())
	Resp11 = forms.ChoiceField(choices=Answer, widget=forms.RadioSelect())
	Resp12 = forms.ChoiceField(choices=Answer, widget=forms.RadioSelect())
	Resp13 = forms.ChoiceField(choices=Answer, widget=forms.RadioSelect())
	Resp14 = forms.ChoiceField(choices=Answer, widget=forms.RadioSelect())
	Resp15 = forms.ChoiceField(choices=Answer, widget=forms.RadioSelect())
	Resp16 = forms.ChoiceField(choices=Answer, widget=forms.RadioSelect())
	Resp17 = forms.ChoiceField(choices=Answer, widget=forms.RadioSelect())
	Resp18 = forms.ChoiceField(choices=Answer, widget=forms.RadioSelect())
	Resp19 = forms.ChoiceField(choices=Answer, widget=forms.RadioSelect())