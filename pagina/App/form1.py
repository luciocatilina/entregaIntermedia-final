from socket import fromshare
from django import forms

class FormularioCurso(forms.Form):

    curso=forms.CharField()

    duracion=forms.IntegerField()

