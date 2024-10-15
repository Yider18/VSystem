from django.shortcuts import render
from .models import Matricula

def lista_matriculas(request):
    matriculas = Matricula.objects.all()
    
    return render(request, 'lista_matriculas.html',{
        'tittle':'matriculas',
        'Matriculas': matriculas})
    
