from django.shortcuts import render

def inicio(request):
    return render(request, 'index.html');

def prueba(request):
    return render(request, 'prueba.html');




