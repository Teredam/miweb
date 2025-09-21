from django.shortcuts import render, redirect
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