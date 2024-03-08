"""
URL configuration for djangocrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls.static import static

#importando el archivo views de la carpeta tasks

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home, name='home'),
    #del archvo views se usara la funcion helloworld
     path('signup/',views.signup, name='signup'),
     path('tasks/',views.tasks, name='tasks'),
     path('tasks_completed/',views.tasks_completed, name='task_completed'),
     path('tasks/create/',views.create_task,name='create_task'),
     #<int:task_id>: significa que es un dato id entero,y se enviara al task_detail
     path('tasks/calificar_tarea/', views.calificar_tarea, name='calificar_tarea'),
     path('tasks/create_nota/',views.create_nota,name='create_nota'),
     path('tasks/notas/', views.nota, name='notas'),
     path('notas/', views.lista_notas, name='notas'),
     path('tasks/<int:task_id>/nota_detail/', views.nota_detail, name='nota_detail'),
     path('tasks/<int:task_id>/complete/',views.complete_task,name='complete_task'),
     path('tasks/<int:task_id>/delete/',views.delete_task,name='delete_task'), 
     path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
     path('tasks/<int:task_id>/',views.task_detail,name='task_detail'),
     path('notas/<int:nota_id>/', views.nota_detail, name='nota_detail'),
     path('notas/<int:nota_id>/complete/', views.complete_nota, name='complete_nota'),
     path('notas/<int:nota_id>/delete/', views.delete_nota, name='delete_nota'),

     path('logout/',views.signout,name='logout'),
     path('signin/',views.signin,name='signin'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#Django pueda servir los archivos estáticos 
