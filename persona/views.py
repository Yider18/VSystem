from django.shortcuts import render,redirect
from django.http import HttpResponse, JsonResponse
from .models import Persona
from matricula.models import Matricula
from persona.models import EstudianteCurso 
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
    
def formulario_matricula(request):
    if request.method == 'POST':
        estudiante_curso_id = request.POST['estudiante_curso']
        fecha_inicio = request.POST['fecha_inicio']
        estado = request.POST['estado']
        costo = request.POST['costo']

        matricula = Matricula(
            estudiante_curso_id=estudiante_curso_id,
            fecha_inicio=fecha_inicio,
            estado=estado,
            costo=costo
        )
        matricula.save()  
        return redirect('formulario')  

    estudiantes_cursos = EstudianteCurso.objects.all()  
    return render(request, 'formulario.html', {'estudiantes_cursos': estudiantes_cursos})
