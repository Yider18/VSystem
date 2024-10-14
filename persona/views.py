from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .models import Persona
from .models import EstudianteCurso 
from curso.models import Curso

def formulario (request):
     if request.method == 'POST':
         nombre= request.POST['nombre']
         apellidos= request.POST['apellidos']
         dni= request.POST['dni']
         telefono= request.POST['telefono']
         email= request.POST['email']
         fecha_nacimiento= request.POST['fecha_nacimiento']
         rol= request.POST['rol']
         persona = Persona(
            nombre=nombre,
            apellidos=apellidos,
            dni=dni,
            telefono=telefono,
            email=email,
            fecha_nacimiento=fecha_nacimiento,
            rol=rol
        )
         persona= persona.save();
     return render(request, 'formulario.html')

def get_estudiantes(request):

    estudiantes = Persona.objects.filter(rol='estudiante');
    

    return render(request, 'lista-estudiantes.html', {
            'tittle': 'Lista de Estudiantes',
            'estudiantes': estudiantes
        })
    

def Estudiantecurso(request):

    Estudiantes_Curso = EstudianteCurso.objects.filter(Estudiante_id__rol='estudiante');
    

    return render(request, 'Estudiante_curso.html', {
            'tittle': 'Estudiante_Curso',
            'EstudiantesC': Estudiantes_Curso
        })