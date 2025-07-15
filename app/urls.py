from django.urls import path
from app.views import login_view
from django.contrib.auth.views import LogoutView
from django.contrib.auth import views as auth_views
from .views import (
    inicio, buscar_medicamento,
    MedicamentoCreateView, MedicamentoListView, MedicamentoDetailView, MedicamentoUpdateView, MedicamentoDeleteView,
    FarmaceuticoCreateView, FarmaceuticoListView, FarmaceuticoDetailView, FarmaceuticoUpdateView, FarmaceuticoDeleteView,
    EntregableCreateView, EntregableListView, EntregableDetailView, EntregableUpdateView, EntregableDeleteView,
    RegistroView, perfil, editar_perfil, cambiar_password, CustomLogoutView, AboutView )

urlpatterns = [
    path('', inicio, name='inicio'),

    # Medicamentos
    path('medicamento/crear/', MedicamentoCreateView.as_view(), name='crear_medicamento'),
    path('medicamento/listar/', MedicamentoListView.as_view(), name='listar_medicamentos'),
    path('medicamento/<int:pk>/', MedicamentoDetailView.as_view(), name='detalle_medicamento'),
    path('medicamento/<int:pk>/editar/', MedicamentoUpdateView.as_view(), name='editar_medicamento'),
    path('medicamento/<int:pk>/eliminar/', MedicamentoDeleteView.as_view(), name='eliminar_medicamento'),

    # Farmacéuticos
    path('farmaceutico/crear/', FarmaceuticoCreateView.as_view(), name='crear_farmaceutico'),
    path('farmaceutico/listar/', FarmaceuticoListView.as_view(), name='listar_farmaceuticos'),
    path('farmaceutico/<int:pk>/', FarmaceuticoDetailView.as_view(), name='detalle_farmaceutico'),
    path('farmaceutico/<int:pk>/editar/', FarmaceuticoUpdateView.as_view(), name='editar_farmaceutico'),
    path('farmaceutico/<int:pk>/eliminar/', FarmaceuticoDeleteView.as_view(), name='eliminar_farmaceutico'),

    # Entregables
    path('entregable/crear/', EntregableCreateView.as_view(), name='crear_entregable'),
    path('entregable/listar/', EntregableListView.as_view(), name='listar_entregables'),
    path('entregable/<int:pk>/', EntregableDetailView.as_view(), name='detalle_entregable'),
    path('entregable/<int:pk>/editar/', EntregableUpdateView.as_view(), name='editar_entregable'),
    path('entregable/<int:pk>/eliminar/', EntregableDeleteView.as_view(), name='eliminar_entregable'),

    # Búsqueda
    path('buscar-medicamento/', buscar_medicamento, name='buscar_medicamento'),
    
    # Registro y Login/Logout
    path('register/', RegistroView.as_view(), name='register'),
    path('logout/', CustomLogoutView.as_view(next_page='inicio'), name='logout'),
    path('login/', login_view, name='login'),


    # Perfil y gestión
    path('perfil/', perfil, name='perfil'),
    path('perfil/editar/', editar_perfil, name='editar_perfil'),
    path('perfil/cambiar-password/', cambiar_password, name='cambiar_password'),


    

   path("about/", AboutView.as_view(), name="about"),

]
