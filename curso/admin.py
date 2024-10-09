from django.contrib import admin
from .models import Curso
admin.site.register(Curso)

class CursoAdmin(admin.ModelAdmin):
    list_display = ('Nombre','Capacidad','Profesor')
