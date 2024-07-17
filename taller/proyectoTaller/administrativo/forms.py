from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _
from django import forms

from administrativo.models import Edificio, Departamento

class EdificioForm(ModelForm):
    class Meta:
        model = Edificio
        fields = ['nombre', 'direccion', 'ciudad', 'tipo']
        labels = {
            'nombre': _('Ingrese el nombre del edificio:'),
            'direccion': _('Ingrese la direccion:'),
            'ciudad': _('Ingrese la ciudad a la que pertenece:'),
            'tipo': _('Seleccione el tipo:'),
        }


class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre', 'costo', 'nCuartos', 'edificio']
        labels = {
            'nombre': _('Ingrese el nombre completo del propietario'),
            'costo': _('Ingrese el costo del departamento'),
            'nCuartos': _('Ingrese el Número de cuartos'),
            'edificio': _('Seleccione edificio'),
        }
    

