"""Proyecto2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from principal.views import formmedico, login, vermedico, loginC, registro, guardarPaciente, validarUsuarioP, errorloginC, verpaciente, agendar, guardarAgendar, verHora, loginM, validarUsuarioM, loginS, validarUsuarioS, vermedico2, guardarMedico, eliminarMedico, eliminarHora, modificarMedico, modificarGuardarMedico, modificarHora, modificarGuardarHora
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('formM', formmedico),
    path('verM', vermedico),
    path('verP', verpaciente),
    path('', login),
    path('loginC', loginC),
    path('registro', registro),
    path('guardarPaciente', guardarPaciente),
    path('validarUsuarioP', validarUsuarioP),
    path('errorloginC', errorloginC),
    path('agendar', agendar),
    path('guardarAgendar', guardarAgendar),
    path('verH', verHora),
    path('loginM', loginM),
    path('validarUsuarioM', validarUsuarioM),
    path('loginS', loginS),
    path('validarUsuarioS', validarUsuarioS),
    path('verM2', vermedico2),
    path('guardarMedico', guardarMedico),
    path('eliminarM/<int:v_idMedico>', eliminarMedico),
    path('eliminarH/<int:v_idHora>', eliminarHora),
    path('modificarM/<int:v_idMedico>', modificarMedico),
    path('guardarM', modificarGuardarMedico),
    path('modificarH/<int:v_idHora>', modificarHora),
    path('guardarH', modificarGuardarHora),
]
