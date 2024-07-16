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

    def clean_ciudad(self):
        valor = self.cleaned_data['ciudad']
        if valor.startswith('L'):
            raise forms.ValidationError("El nombre de la ciudad no puede iniciar con la letra mayúscula L")
        return valor

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

    def clean_nombre(self):
        valor = self.cleaned_data['nombre']
        num_palabras = len(valor.split())
        if num_palabras < 3:
            raise forms.ValidationError("El nombre de un propietario no debe tener menos de 3 palabras.")
        return valor

    def clean_costo(self):
        valor = self.cleaned_data['costo']
        if valor > 100000:
            raise forms.ValidationError("El costo de un departamento no puede ser mayor a $100 mil.")
        return valor

    def clean_nCuartos(self):
        valor = self.cleaned_data['nCuartos']
        if valor == 0 or valor > 7:
            raise forms.ValidationError("El número de cuartos no puede ser 0, ni mayor a 7.")
        return valor
    

