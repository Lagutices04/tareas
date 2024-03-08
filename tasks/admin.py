

from django.contrib import admin
from .models import Task, Calificacion

class TaskAdmin(admin.ModelAdmin):
    list_display = ['pk','title', 'field', 'created', 'datecompleted', 'important', 'user']

try:
    admin.site.register(Task, TaskAdmin)
except admin.sites.AlreadyRegistered:
  pass


class CalificarAdmin(admin.ModelAdmin):
    list_display=['pk','mark1','mark2','mark3','average']
try:
 admin.site.register(Calificacion,CalificarAdmin)
except admin.sites.AlreadyRegistred:
        pass
