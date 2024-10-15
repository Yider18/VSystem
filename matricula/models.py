from django.db import models


class Matricula(models.Model):
    estudiante_curso = models.ForeignKey('persona.EstudianteCurso', on_delete=models.PROTECT) 
    fecha_inicio = models.DateField()
    estado = models.CharField(max_length=20)
    costo = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
          return f'{self.estudiante_curso.Estudiante_id} {self.fecha_inicio} - {self.estado} - {self.costo}'

class Meta:
        db_table = 'Matricula' 