from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('mensajes/', views.lista_contactos, name='lista_contactos'),
    path("servicios/", views.servicios, name="servicios"),
    path("sobre/", views.sobre, name="sobre"),
    path("contacto/", views.contacto, name="contacto"),
    path("registro/", views.registro, name="registro"),
    path("dashboard/", views.dashboard, name="dashboard"),

     # Login y logout usando las vistas de Django
    path("login/", auth_views.LoginView.as_view(template_name="inicio/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),

    # Cambio de contraseña
    path("password_change/", auth_views.PasswordChangeView.as_view(template_name="inicio/password_change.html"), name="password_change"),
    path("password_change/done/", auth_views.PasswordChangeDoneView.as_view(template_name="inicio/password_change_done.html"), name="password_change_done"),
]

