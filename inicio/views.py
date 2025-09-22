from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseForbidden
from .forms import ContactoForm
from .models import Contacto

def home(request):
    if request.method == "POST":
        form = ContactoForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "inicio/home.html", {"form": ContactoForm(), "success": True})
    else:
        form = ContactoForm()

    return render(request, "inicio/home.html", {"form": form})

def lista_contactos(request):
    contactos = Contacto.objects.all().order_by('-id')  # últimos primero
    return render(request, "inicio/lista.html", {"contactos": contactos})

def eliminar_contacto(request, id):
    contacto = Contacto.objects.get(id=id)
    contacto.delete()
    return redirect("lista_contactos")

def home(request):
    return render(request, "inicio/home.html")

def servicios(request):
    return render(request, "inicio/servicios.html")

def sobre(request):
    return render(request, "inicio/sobre.html")

def contacto(request):
    return render(request, "inicio/contacto.html")

# Registro de usuarios
def registro(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")  # Después del registro va a login
    else:
        form = UserCreationForm()
    return render(request, "inicio/registro.html", {"form": form})

# Dashboard (solo si estás logueado)
@login_required
def dashboard(request):
    user = request.user
    if user.is_superuser:
        role = "superadmin"
    elif user.is_staff:
        role = "staff"
    else:
        role = "usuario"
    return render(request, "inicio/dashboard.html", {"role": role})

@login_required
def lista_contactos(request):
    if not request.user.is_staff:
        return HttpResponseForbidden("No tienes permiso para ver esta página.")
    contactos = Contacto.objects.all().order_by("-id")
    return render(request, "inicio/lista.html", {"contactos": contactos})