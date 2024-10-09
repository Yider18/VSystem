from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Curso

def curso(request):
    
    curso = Curso.objects.filter(profesor__rol='profesor');
    return render(request, 'curso.html',{
        'tittle': 'Lista de cursos',
        'curso': curso
    })

