from django import forms
from django.forms import ModelForm
from .models import *
from .forms import *
from datetime import date

from django.contrib.auth.forms import UserCreationForm

class RegistroForm(UserCreationForm):
    roles = (
    (Usuario.RECEPCIONISTA, 'recepcionista'),
    (Usuario.CUIDADOR , 'cuidador'),
    (Usuario.CLIENTE , 'cliente'),
)

    rol = forms.ChoiceField(choices=roles)
    class Meta:
        model = Usuario
        fields = ('username', 'email', 'password1', 'password2', 'rol')


