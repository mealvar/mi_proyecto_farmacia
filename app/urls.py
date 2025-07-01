from django.urls import path
from .views import inicio,crear_medicamento, crear_farmaceutico,crear_entregable,buscar_medicamento

urlpatterns = [
    path('', inicio, name='inicio'),                    
    path('medicamento/', crear_medicamento, name='crear_medicamento') , 
    path('farmaceutico/', crear_farmaceutico, name='crear_farmaceutico') ,
    path('entregable/', crear_entregable, name='crear_entregable'),
    path('buscar-medicamento/', buscar_medicamento, name='buscar_medicamento'),
    
]


