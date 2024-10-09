from django.db import models
from persona.models import Persona
from django.core.exceptions import ValidationError


class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    capacidad = models.IntegerField()
    profesor = models.ForeignKey(Persona, on_delete=models.PROTECT, limit_choices_to={'rol': 'profesor'})
    
    def save(self,*args,**kwargs):
        if self.profesor.rol != 'profesor':
            raise ValidationError ('el rol del profesor debe ser docente')
        super().save(*args,**kwargs)
       
    
    def clean(self):
        if self.capacidad <= 0:
            raise ValidationError('Capacidad no puede ser negativa')
        
    def Meta(self):
        db_table = 'curso'
         
        
    
    
    
    
