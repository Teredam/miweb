# 🌐 MiWeb - Proyecto Django listo para Render

[![Render Status](https://img.shields.io/badge/render-online-brightgreen?logo=render)](https://miweb-2y99.onrender.com)
[![Python](https://img.shields.io/badge/python-3.10+-blue?logo=python)](https://www.python.org/)
[![Django](https://img.shields.io/badge/django-5.x-green?logo=django)](https://www.djangoproject.com/)


                 ┌──────────────┐
                 │  Visitante   │
                 └──────┬──────┘
                        │
                ┌───────▼────────┐
                │ Página Inicio  │
                └───────┬────────┘
                        │
    ┌───────────────┬───┼───────────────┬───────────────┐
    ▼               ▼   ▼               ▼               ▼
Servicios         Sobre  Contacto     Registro         Login
                                    (crea usuario)  (autentica)

                   ┌───────────────┐
                   │   Dashboard   │
                   └───────┬───────┘
                           │
             ┌─────────────┴─────────────┐
             ▼                           ▼
        Usuario normal                Staff/Admin
        ┌───────────────┐             ┌───────────────┐
        │ Cambiar pass  │             │ Lista mensajes│
        │ Ver info user │             │ Dashboard full│
        └───────────────┘             └───────────────┘

        | Página             | Visitante | Usuario | Staff/Admin |
        | ------------------ | --------- | ------- | ----------- |
        | Inicio             |     ✅    |   ✅   |      ✅     |
        | Servicios          |     ✅    |   ✅   |      ✅     |
        | Sobre nosotros     |     ✅    |   ✅   |      ✅     |
        | Contacto           |     ✅    |   ✅   |      ✅     |
        | Registro           |     ✅    |   ❌   |      ❌     |
        | Login              |     ✅    |   ❌   |      ❌     |
        | Dashboard          |     ❌    |   ✅   |      ✅     |
        | Cambiar contraseña |     ❌    |   ✅   |      ✅     |
        | Lista de mensajes  |     ❌    |   ❌   |      ✅     |

