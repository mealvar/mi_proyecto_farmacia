from django.db import models
from django import forms
from django.contrib.auth.models import User


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
    nombre = models.CharField(max_length=100)  # CharField 1
    droga = models.CharField(max_length=100)   # CharField 2
    descripcion = models.TextField()            # texto plano
    stock = models.IntegerField()
    imagen = models.ImageField(upload_to='medicamentos/', blank=True, null=True)
    fecha_creacion = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nombre

class MedicamentoFormulario(forms.ModelForm):
    class Meta:
        model = Medicamento
        fields = ['nombre', 'droga', 'stock']


class Perfil(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil')
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    biografia = models.TextField(blank=True)
    link = models.URLField(blank=True)
    fecha_cumpleanos = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"Perfil de {self.user.username}"