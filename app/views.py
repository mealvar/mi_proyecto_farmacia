from django.shortcuts import render, redirect
from .models import Farmaceutico, Entregable, Medicamento
from app.forms import FarmaceuticoFormulario, MedicamentoFormulario, EntregableFormulario
from django.http import HttpResponse
from .forms import BusquedaMedicamentoFormulario 


def inicio(request):
    return render(request, "app/index.html")

def crear_medicamento(request):
    if request.method == "POST":
        form = MedicamentoFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio') 
    else:
        form = MedicamentoFormulario()
    return render(request, "formulario/formulario.html", {"formulario": form, "titulo": "Medicamento"})

def crear_farmaceutico(request):
    if request.method == "POST":
        form = FarmaceuticoFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = FarmaceuticoFormulario()
    
    return render(request, "formulario/formulario.html", {"formulario": form, "titulo": "Farmacéutico"})

def crear_entregable(request):
    if request.method == "POST":
        form = EntregableFormulario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('inicio')
    else:
        form = EntregableFormulario()
    
    return render(request, "formulario/formulario.html", {"formulario": form, "titulo": "Entrega"})


def buscar_medicamento(request):
    resultados = []
    if request.method == "GET":
        formulario = BusquedaMedicamentoFormulario(request.GET)
        if formulario.is_valid():
            nombre = formulario.cleaned_data["nombre"]
            resultados = Medicamento.objects.filter(nombre__icontains=nombre)
    else:
        formulario = BusquedaMedicamentoFormulario()

    return render(request, "formulario/busqueda.html", {
        "formulario": formulario,
        "resultados": resultados,
        "titulo": "Buscar Medicamento"
    })