from django.shortcuts import render, redirect
from django.contrib.auth import login, update_session_auth_hash, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Farmaceutico, Entregable, Medicamento, Perfil
from .forms import (
    FarmaceuticoFormulario,
    MedicamentoFormulario,
    EntregableFormulario,
    BusquedaMedicamentoFormulario,
    UserForm,
    PerfilForm,
    CustomUserCreationForm,
)

def inicio(request):
    return render(request, "app/index.html")


class RegistroView(CreateView):
    form_class = CustomUserCreationForm
    template_name = "registration/register.html"
    success_url = reverse_lazy("inicio")

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)  
        messages.success(self.request, f"¡Bienvenido/a, {user.username}!")
        return super().form_valid(form)




# --- Medicamento CBVs --- 

class MedicamentoCreateView(LoginRequiredMixin, CreateView):
    model = Medicamento
    form_class = MedicamentoFormulario
    template_name = "app/medicamento_form.html"
    success_url = reverse_lazy("listar_medicamentos")
    extra_context = {"titulo": "Agregar Medicamento"}

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Medicamento agregado con éxito")
        return response



class MedicamentoListView(LoginRequiredMixin,ListView):
    model = Medicamento
    template_name = "medicamento/medicamento_list.html"
    context_object_name = "medicamentos"


class MedicamentoDetailView(DetailView):
    model = Medicamento
    template_name = "app/medicamento_detail.html"
    context_object_name = "medicamento"


class MedicamentoUpdateView(LoginRequiredMixin, UpdateView):
    model = Medicamento
    form_class = MedicamentoFormulario
    template_name = "formulario/formulario.html"
    success_url = reverse_lazy("listar_medicamentos")
    extra_context = {"titulo": "Editar Medicamento"}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formulario"] = context.pop("form")
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Medicamento editado con éxito")
        return response


class MedicamentoDeleteView(LoginRequiredMixin, DeleteView):
    model = Medicamento
    template_name = "app/medicamento_delete.html"  
    success_url = reverse_lazy("listar_medicamentos")
     
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Medicamento eliminado con éxito")
        return super().delete(request, *args, **kwargs)


# --- Farmaceutico CBVs y funciones ---


from django.contrib import messages

class FarmaceuticoCreateView(LoginRequiredMixin, CreateView):
    model = Farmaceutico
    form_class = FarmaceuticoFormulario
    template_name = "app/farmaceutico_form.html"
    success_url = reverse_lazy("listar_farmaceuticos")

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Farmacéutico agregado con éxito")
        return response
    

class FarmaceuticoListView(LoginRequiredMixin, ListView):
    model = Farmaceutico
    template_name = "app/farmaceutico_list.html"
    context_object_name = "farmaceuticos"

class FarmaceuticoDetailView(DetailView):
    model = Farmaceutico
    template_name = "app/farmaceutico_detail.html"
    context_object_name = "farmaceutico"


class FarmaceuticoUpdateView(LoginRequiredMixin, UpdateView):
    model = Farmaceutico
    form_class = FarmaceuticoFormulario
    template_name = "formulario/formulario.html"
    success_url = reverse_lazy("listar_farmaceuticos")
    extra_context = {"titulo": "Editar Farmacéutico"}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formulario"] = context.pop("form")
        # Aquí podés sobrescribir 'titulo' para asegurarte que venga en el contexto:
        context["titulo"] = "Editar Farmacéutico"
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Farmacéutico editado con éxito")
        return response
    

class FarmaceuticoDeleteView(LoginRequiredMixin, DeleteView):
    model = Farmaceutico
    template_name = "app/farmaceutico_delete.html"
    success_url = reverse_lazy("listar_farmaceuticos")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Farmacéutico eliminado con éxito")
        return super().delete(request, *args, **kwargs)


# --- Entregable CBVs y funciones ---

class EntregableCreateView(LoginRequiredMixin, CreateView):
    model = Entregable
    fields = ["nombre", "descripcion"]
    template_name = "app/entregable_form.html"
    success_url = reverse_lazy("listar_entregables")
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formulario"] = context.pop("form")
        context["titulo"] = "Entrega"
        context["verbo"] = "Agregar"
        return context

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Entrega solicitada con éxito")
        return response


class EntregableListView(LoginRequiredMixin,ListView):
    model = Entregable
    template_name = "entregable/entregable_list.html"
    context_object_name = "entregables"


class EntregableDetailView(DetailView):
    model = Entregable
    template_name = "app/entregable_detail.html"
    context_object_name = "entregable"


class EntregableUpdateView(LoginRequiredMixin, UpdateView):
    model = Entregable
    form_class = EntregableFormulario
    template_name = "formulario/formulario.html"
    success_url = reverse_lazy("listar_entregables")
    extra_context = {"titulo": "Editar Entrega"}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["formulario"] = context.pop("form")
        return context
    
    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Entrega editada con éxito")
        return response


class EntregableDeleteView(LoginRequiredMixin, DeleteView):
    model = Entregable
    template_name = "app/entregable_delete.html"
    success_url = reverse_lazy("listar_entregables")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Entregable eliminado con éxito")
        print("Mensaje de éxito agregado")
        return super().delete(request, *args, **kwargs)


@login_required
def buscar_medicamento(request):
    resultados = []
    nombre = None
    error = None
    formulario = BusquedaMedicamentoFormulario(request.GET or None)

    if formulario.is_valid():
        nombre = formulario.cleaned_data.get("nombre")
        if nombre:
            resultados = Medicamento.objects.filter(nombre__icontains=nombre).order_by("nombre")
            if not resultados:
                error = f"No se encontraron medicamentos con '{nombre}'."
        else:
            error = "Por favor ingresá un término para buscar."

    return render(request, "formulario/busqueda.html", {
        "formulario": formulario,
        "resultados": resultados,
        "nombre": nombre,
        "error": error,
    })

# --- Perfil, edición y cambio de contraseña ---

@login_required
def perfil(request):
    return render(request, "perfil/perfil.html")


@login_required
def editar_perfil(request):
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        perfil_form = PerfilForm(request.POST, request.FILES, instance=request.user.perfil)
        if user_form.is_valid() and perfil_form.is_valid():
            user_form.save()
            perfil_form.save()
            messages.success(request, "Perfil actualizado correctamente.")
            return redirect("perfil")
    else:
        user_form = UserForm(instance=request.user)
        perfil_form = PerfilForm(instance=request.user.perfil)

    return render(
        request,
        "perfil/editar_perfil.html",
        {"user_form": user_form, "perfil_form": perfil_form},
    )


@login_required
def cambiar_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Contraseña actualizada correctamente.")
            return redirect("perfil")
        else:
            print(form.errors)
    else:
        form = PasswordChangeForm(request.user)
    return render(request, "perfil/cambiar_password.html", {"form": form})


# --- Login y logout ---

def login_view(request):
    next_url = request.GET.get('next', '')
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        next_url = request.POST.get("next")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Bienvenido/a, {user.username}")
            return redirect(next_url or "inicio")
        else:
            messages.error(request, "Usuario o contraseña incorrectos.")
    return render(request, "registration/login.html", {"next": next_url})


from django.contrib.auth.views import LogoutView

class CustomLogoutView(LogoutView):
    def get(self, request, *args, **kwargs):
        # Permite hacer logout con GET
        return self.post(request, *args, **kwargs)



#---------------

class AboutView(TemplateView):
    template_name = "app/about.html"
