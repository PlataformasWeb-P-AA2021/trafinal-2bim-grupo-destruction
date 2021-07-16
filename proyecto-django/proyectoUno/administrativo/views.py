from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# ejemplo de uso django-rest_framework
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from administrativo.serializers import UserSerializer, GroupSerializer, \
PersonaSerializer, BarrioSerializer, CasaSerializer, DepartamentoSerializer

# importar las clases de models.py
from administrativo.models import *

# importar los formularios de forms.py
from administrativo.forms import *

def index(request):
    casas = Casa.objects.all()
    departamentos = Departamento.objects.all()
    informacion_template = {'casas': casas, 'numero_casas': len(casas), \
    'departamentos': departamentos, 'numero_departamentos': len(departamentos)}

    return render(request, 'index.html', informacion_template)

# PERSONA

def obtener_persona(request, id):

    persona = Persona.objects.get(pk=id)
    informacion_template = {'persona': persona}
    return render(request, 'obtener_persona.html', informacion_template)


def crear_persona(request):

    if request.method=='POST':
        formulario = PersonaForm(request.POST)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(index)
    else:
        formulario = PersonaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_persona.html', diccionario)


def editar_persona(request, id):
    
    persona = Persona.objects.get(pk=id)
    if request.method=='POST':
        formulario = PersonaForm(request.POST, instance=persona)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = PersonaForm(instance=persona)
    diccionario = {'formulario': formulario}

    return render(request, 'editar_persona.html', diccionario)


def eliminar_persona(request, id):

    persona = Persona.objects.get(pk=id)
    persona.delete()
    return redirect(index)


# BARRIO

def obtener_barrio(request, id):

    barrio = Barrio.objects.get(pk=id)
    informacion_template = {'barrio': barrio}
    return render(request, 'obtener_barrio.html', informacion_template)


def crear_barrio(request):

    if request.method=='POST':
        formulario = BarrioForm(request.POST)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(index)
    else:
        formulario = BarrioForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_barrio.html', diccionario)


def editar_barrio(request, id):
    
    barrio = Barrio.objects.get(pk=id)
    if request.method=='POST':
        formulario = BarrioForm(request.POST, instance=barrio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = BarrioForm(instance=barrio)
    diccionario = {'formulario': formulario}

    return render(request, 'editar_barrio.html', diccionario)


def eliminar_barrio(request, id):

    barrio = Barrio.objects.get(pk=id)
    barrio.delete()
    return redirect(index)


#------------------------------------------------

# DEPARTAMENTO

def obtener_departamento(request, id):

    departamento = Departamento.objects.get(pk=id)
    informacion_template = {'departamento': departamento}
    return render(request, 'obtener_departamento.html', informacion_template)

def crear_departamento(request):

    if request.method=='POST':
        formulario = DepartamentoForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = DepartamentoForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_departamento.html', diccionario)


def editar_departamento(request, id):

    departamento = Departamento.objects.get(pk=id)
    if request.method=='POST':
        formulario = DepartamentoForm(request.POST, instance=departamento)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = DepartamentoForm(instance=departamento)
    diccionario = {'formulario': formulario}

    return render(request, 'editar_departamento.html', diccionario)

def eliminar_departamento(request, id):

    departamento = Departamento.objects.get(pk=id)
    departamento.delete()
    return redirect(index)

# CASA

def obtener_casa(request, id):

    casa = Casa.objects.get(pk=id)
    informacion_template = {'casa': casa}
    return render(request, 'obtener_casa.html', informacion_template)

def crear_casa(request):

    if request.method=='POST':
        formulario = CasaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = CasaForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_casa.html', diccionario)


def editar_casa(request, id):
    """
    """
    casa = Casa.objects.get(pk=id)
    if request.method=='POST':
        formulario = CasaForm(request.POST, instance=casa)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = CasaForm(instance=casa)
    diccionario = {'formulario': formulario}

    return render(request, 'editar_casa.html', diccionario)

def eliminar_casa(request, id):

    casa = Casa.objects.get(pk=id)
    casa.delete()
    return redirect(index)

# crear vistas a través de viewsets
class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):

    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]

class PersonaViewSet(viewsets.ModelViewSet):

    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
    permission_classes = [permissions.IsAuthenticated]


class BarrioViewSet(viewsets.ModelViewSet):

    queryset = Barrio.objects.all()
    serializer_class = BarrioSerializer
    permission_classes = [permissions.IsAuthenticated]

class DepartamentoViewSet(viewsets.ModelViewSet):

    queryset = Departamento.objects.all()
    serializer_class = DepartamentoSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class CasaViewSet(viewsets.ModelViewSet):

    queryset = Casa.objects.all()
    serializer_class = CasaSerializer
    permission_classes = [permissions.IsAuthenticated]


