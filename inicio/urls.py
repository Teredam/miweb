from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mensajes/', views.lista_contactos, name='lista_contactos'),
]

