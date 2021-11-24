from django import forms
from django.forms import ModelForm
from .models import UsuarioP

class usuarioPForm(ModelForm):

    class Meta:
        model= UsuarioP
        fields =['email', 'nombre', 'password']