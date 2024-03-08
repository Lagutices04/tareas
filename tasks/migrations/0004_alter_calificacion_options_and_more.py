# Generated by Django 5.0.1 on 2024-03-05 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_calificacion_mark'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='calificacion',
            options={'verbose_name': 'nota', 'verbose_name_plural': 'notas'},
        ),
        migrations.RenameField(
            model_name='calificacion',
            old_name='usuario',
            new_name='student',
        ),
        migrations.RemoveField(
            model_name='calificacion',
            name='calificacion',
        ),
        migrations.RemoveField(
            model_name='calificacion',
            name='tarea',
        ),
        migrations.AddField(
            model_name='calificacion',
            name='average',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, verbose_name='promedio'),
        ),
        migrations.AddField(
            model_name='calificacion',
            name='mark1',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='nota1'),
        ),
        migrations.AddField(
            model_name='calificacion',
            name='mark2',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='nota2'),
        ),
        migrations.AddField(
            model_name='calificacion',
            name='mark3',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='nota3'),
        ),
        migrations.DeleteModel(
            name='Mark',
        ),
    ]