from django.shortcuts import render
from .models import *
from django.http import HttpResponse
from .form1 import *

# Create your views here.

def cursos(request):

    if request.method=='POST':
        formulario1=FormularioCurso(request.POST)

        if formulario1.is_valid():
            info=formulario1.cleaned_data()
            cursoF=Curso(nombre=info['curso'], duracion=info['duracion'])
            cursoF.save()
            return render(request, 'App/cursos.html')
        else:
            formulario1=FormularioCurso()
    else:
        return render(request, 'App/cursos.html')

def profesores(request):
    '''
    if request.method=='POST':

        profesor=Profesor(
            nombre=request.POST['nombre'],
            email=request.POST[]
        )
    '''

def ubicacion(request):

    lugar1=Ubicacion(nombre='Lanus', cantAlumnos='78')
    lugar2=Ubicacion(nombre='Almagro', cantAlumnos='178')
    lugar3=Ubicacion(nombre='Avellaneda', cantAlumnos='59')
    lugar4=Ubicacion(nombre='Palermo', cantAlumnos='113')

    lugar1.save()
    lugar2.save()
    lugar3.save()
    lugar4.save()

    return render(request, 'App/busquedaLugar.html')

def buscar(request):

    if request.GET['cantAlumnos']:
        busqueda=request.GET['cantAlumnos']
        lugar=Ubicacion.objetcs.filter(cantAlumnos__icontains=busqueda)
        return render(request, 'App/resultados.html')
    else:
        mensaje='no existe esa ubicacion'
        return HttpResponse(mensaje)