from django import forms
from .models import Medicamento,Farmaceutico, Entregable

class FarmaceuticoFormulario(forms.ModelForm):
    class Meta:
        model = Farmaceutico
        fields = ['nombre', 'apellido', 'email']

class MedicamentoFormulario(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['nombre', 'droga', 'stock']


class EntregableFormulario(forms.ModelForm):
    class Meta:
        model = Entregable
        fields = ['nombre', 'descripcion']

class BusquedaMedicamentoFormulario(forms.Form):
    nombre = forms.CharField(max_length=100, required=False, label='Buscar Medicamento')        