# Generated by Django 5.1 on 2024-10-15 01:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matricula', '0001_initial'),
        ('persona', '0002_estudiantecurso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matricula',
            name='estudiante_curso',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='persona.estudiantecurso'),
        ),
    ]
