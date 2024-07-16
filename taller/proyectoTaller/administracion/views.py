from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render

# importar las clases de models.py
from administrativo.models import *

# importar los formularios de forms.py
from administrativo.forms import *

def index(request):
    edificio = Edificio.objects.all()
    diccionario = {
        'edificio': edificio
    }
    return render(request, 'index.html', diccionario)

def obtener_edificio(request, id):
    edificio = Edificio.objects.get(pl=id)
    diccionario = {
        'edificio': edificio
    }
    return render(request, 'obtener_edificio.html', diccionario)



## ---------------- crear
def crear_edificio(request):
    if request.method=='POST':
        formulario = EdificioForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(index)
    else:
        formulario = EdificioForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_edificio.html', diccionario)

def crear_departamento(request):
    if request.method=='POST':
        formulario = DepartamentoForm(request.POST)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save() # se guarda en la base de datos
            return redirect(index)
    else:
        formulario = DepartamentoForm()
    diccionario = {'formulario': formulario}

    return render(request, 'crear_departamento.html', diccionario)

## ---------------- editar
def editar_edificio(request, id):
    edificio = Edificio.objects.get(pk=id)
    if request.method=='POST':
        formulario = EdificioForm(request.POST, instance=edificio)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = EdificioForm(instance=edificio)
    diccionario = {'formulario': formulario}

    return render(request, 'editar_edificio.html', diccionario)

def editar_departamento(request, id):
    departamento = Departamento.objects.get(pk=id)
    if request.method=='POST':
        formulario = DepartamentoForm(request.POST, instance=departamento)
        print(formulario.errors)
        if formulario.is_valid():
            formulario.save()
            return redirect(index)
    else:
        formulario = DepartamentoForm(instance=departamento)
    diccionario = {'formulario': formulario}

    return render(request, 'editar_departamento.html', diccionario)   

## ---------------- eliminar
def eliminar_edificio(request, id):
    edificio = Edificio.objects.get(pk=id)
    edificio.delete()
    return redirect(index)

def eliminar_departamento(request, id):
    departamento = Departamento.objects.get(pk=id)
    departamento.delete()
    return redirect(index)