from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

def index(request):
    return render(request,'core/index.html')

def saludar(request):
    return HttpResponse("Hola desde Django")

def saludar_con_etiqueta(request):
    return HttpResponse('<h1 style="color:red">Hola </h1> ')

def saludar_con_parametros(request, nombre: str, apellido: str):
    nombre = nombre.capitalize()
    apellido =  apellido.upper()
    return HttpResponse(f'{apellido}, {nombre}')

def probando_template(requests):
     contexto = { 
                    "nombre" : "Maria Elisa" ,
                    "apellido" : "Alvarez" ,
                    "dia" : datetime.now().date,
                    "notas" : [ 10 , 2 , 4 , 7 , 3 ] ,
                    "notas_malas" : [ 6 , 4 , 2 ] , 
                }
     return render(requests,'core/template1.html', contexto)