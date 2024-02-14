from django.db import models
from django.contrib.auth.models import User
#habra una relacion de tablas de tasks con los user generados en views.py

class Task(models.Model):
    #aca creara la tabla
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    field = models.FileField(upload_to='archivos_adjuntos',blank=True, null=True)
    #blanck y null,permite qye estos campos puedan estar vacios en el formulario
    created = models.DateTimeField(auto_now_add=True)
    datecompleted = models.DateTimeField(null=True, blank=True)
    important= models.BooleanField(default=False)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    #si se elimina un dato de user,todo lo q tenga q ver con ese usuario se eliminara en cascada
   
    def __str__(self):
     return f"{self.title} by {self.user.username}"

   #se concardena el titulo de la tarea y el usuario que la envia


    
