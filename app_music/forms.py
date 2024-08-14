from django import forms
from django.views.generic import ListView
from django.views.generic.edit import UpdateView

class CursoFormulario(forms.Form):
    curso = forms.CharField()
    camada = forms.IntegerField()

class BuscaCursoForm(forms.Form):
    curso = forms.CharField()

class EstudianteFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()

class ProfesorFormulario(forms.Form):
    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()