

from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    list_display = ['pk','title', 'field', 'created', 'datecompleted', 'important', 'user']

try:
    admin.site.register(Task, TaskAdmin)
except admin.sites.AlreadyRegistered:
  pass
