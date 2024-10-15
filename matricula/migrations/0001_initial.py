# Generated by Django 5.1 on 2024-10-15 01:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persona', '0002_estudiantecurso'),
    ]

    operations = [
        migrations.CreateModel(
            name='Matricula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_inicio', models.DateField()),
                ('estado', models.CharField(max_length=20)),
                ('costo', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estudiante_curso', models.ForeignKey(limit_choices_to={'rol': 'estudiante'}, on_delete=django.db.models.deletion.PROTECT, to='persona.estudiantecurso')),
            ],
        ),
    ]
