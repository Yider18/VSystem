from django.db import models


class Persona(models.Model):  
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=100)
    dni = models.CharField(max_length=10)
    telefono = models.CharField(max_length=10)
    email = models.EmailField()
    fecha_nacimiento = models.DateField()
    rol = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.nombre} {self.apellidos} - {self.dni} - {self.rol}'

    class Meta:
        db_table = 'persona'
        
        
        
        
class EstudianteCurso(models.Model):  
    Estudiante_id = models.ForeignKey('persona.Persona', on_delete=models.PROTECT, limit_choices_to={'rol': 'estudiante'}) 
    Curso_id = models.ForeignKey('curso.Curso', on_delete=models.PROTECT)
    fecha_inicio = models.DateField()
    fecha_final =models.DateField()
    Estado = models.CharField(max_length=10)
    Nota = models.FloatField()
  
    def __str__(self):
        return f'{self.Estudiante_id} {self.Curso_id} - {self.fecha_inicio} - {self.fecha_final} - {self.Estado} - {self.Nota}'

    class Meta:
        db_table = 'Estudiante_Curso' 