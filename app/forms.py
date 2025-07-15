from django import forms
from .models import Medicamento,Farmaceutico, Entregable, Perfil
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class FarmaceuticoFormulario(forms.ModelForm):
    class Meta:
        model = Farmaceutico
        fields = ['nombre', 'apellido', 'email']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
     }

class MedicamentoFormulario(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['nombre', 'droga', 'stock', 'imagen']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'droga': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'stock': forms.NumberInput(attrs={'class': 'form-control'}),
            'imagen': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class BusquedaMedicamentoFormulario(forms.Form):
    nombre = forms.CharField(
        max_length=100, 
        required=False, 
        label='Buscar Medicamento',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Buscar por nombre...'})
    )


class EntregableFormulario(forms.ModelForm):
    class Meta:
        model = Entregable
        fields = ['nombre', 'descripcion']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['avatar', 'biografia', 'link', 'fecha_cumpleanos']
        widgets = {
            'fecha_cumpleanos': forms.DateInput(attrs={'type': 'date'})  # para mostrar un selector de fecha en HTML
        }


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Correo electrónico")

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Eliminamos el texto de ayuda para que no aparezca en el form
        for field_name in self.fields:
            self.fields[field_name].help_text = ''

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user