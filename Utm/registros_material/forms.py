from django import forms
from django.forms.widgets import ClearableFileInput
from .models import Materiales

class CustomClearableFileInput(ClearableFileInput):

    template_with_clear = '<br> <label for="%(clear_checkbox_id)s">%(clear_checkbox_label)s</label> %(clear)s'

class Materialesforms(forms.ModelForm):
    class Meta:
        model = Materiales
        fields = ['matricula','nombre_alumno','carrera', 'material']
