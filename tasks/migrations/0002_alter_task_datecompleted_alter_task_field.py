# Generated by Django 5.0.1 on 2024-02-07 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='datecompleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='field',
            field=models.FileField(blank=True, null=True, upload_to='archivos_adjuntos'),
        ),
    ]
