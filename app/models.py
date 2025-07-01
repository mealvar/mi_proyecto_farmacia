from django.db import models
from django import forms

class Farmaceutico(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Entregable(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class Medicamento(models.Model):
    nombre = models.CharField(max_length=100)
    droga = models.TextField()
    stock = models.IntegerField()

    def __str__(self):
        return self.nombre

class MedicamentoFormulario(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['nombre', 'droga', 'stock']

