
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
# cuando yo ejecute esta clase UserCreationForm me va a devolver un formulario
#autentication comprobara si el usuario existe
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
#el login creara la cookie
from django.db import IntegrityError
from .forms import TaskForm
from .models import Task
from django.utils import timezone
from django.contrib.auth.decorators import login_required
#protege cualquier funcion



def home(request):
    #el metodo requuest obtiene informacion del cliente q visita la pagina

    return render(request,'home.html')

def signup(request):
    if request.method == 'GET':
        return render(request,'signup.html',{
            'form' : UserCreationForm
        })
        
      
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                 user = User.objects.create_user(username=request.POST['username'],
                password=request.POST['password1'])
                 user.save()
                 login(request,  user)
                #crea las cookies las cuales podremos visualizar cuando inspeccionemos el servidor 
                 return   redirect('tasks')
            except IntegrityError:
                #se consideran excepciones,que estan dedidcadas a un error especifico
                return render(request,'signup.html',{
                    'form': UserCreationForm,
                    "error": 'usuario existente troll'
                })
            
            
               
            #ese return te re direccionara al template tarea si el usuario fue creado correctamente
       
        return    render(request, 'signup.html',{
                    'form': UserCreationForm,
                    "error" : 'contraseña no coincide'
        #etiqueta django que hace formularios desde django al html
    })


@login_required 
def tasks(request):
    
      tasks =Task.objects.filter(user=request.user, datecompleted__isnull=True)
    #devolver todas las tareas de la base de datos
    #filter(user=request.user) esto mostrara solo las tareas que correspondan al usuario que inicio sesion,no vera las tareas de otros usuarios
    #tambien mostrara las tareas que aun no estan completadas
    
      return render(request, 'tasks.html',{'tasks':tasks})
#te pasare el dato al front,con el dato de tareas que se ha consultado

#render espera el parametro request
 #espera usuario y contraseña para guardarlo en ese usuario
         #devolvera un objto user

@login_required         
def tasks_completed(request):    
      tasks =Task.objects.filter(user=request.user, datecompleted__isnull=False).order_by
      ('-datecompleted') 
      #ordena las tareas segun su fecha
      return render(request, 'tasks.html',{'tasks':tasks})


@login_required
def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {'form': TaskForm})
    else:
      try:
            form = TaskForm(request.POST, request.FILES)
            if form.is_valid():
             new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            print(new_task)
            return redirect('tasks')
      except ValueError:
           return render(request, 'create_task.html', {
        'form': TaskForm,
        'error': 'Por favor, envía datos válidos'
    })

@login_required
def task_detail(request, task_id):
    if request.method == 'GET':
        task= get_object_or_404 (Task,pk=task_id, user=request.user)
    #del modelo tareas voy a obtener un dato,donde la primary key sea igual al parametro task_id
    #ese get objects, cuando muestre un error 404 no tumbara todo el servidor
        form =TaskForm(instance=task)
    #el va a llenar el formulario con esa tarea
        return render(request, 'task_detail.html', {'task':task, 'form': form})
#retornara al template task detail y con esto {'task':task}) lo mostrara como un diccionario
    else:
        try:
            task = get_object_or_404(Task,pk=task_id, user=request.user)
            form= TaskForm(request.POST, instance=task)
     #esto permitira actualizar las tareas
            form.save()
            return redirect('tasks')
        except ValueError:
            return render (request, 'task_detail',{'task':task,'form':form, 'error':'error al momento de actializar la tarea miau'})

@login_required
def complete_task(request,task_id):
  task =  get_object_or_404(Task, pk=task_id, user=request.user )
  #buscara la tarea por el primari key osea el id de la tarea
  #y solamente mostrara la tarea de ese id
  if request.method == 'POST':
      task.datecompleted = timezone.now()
      task.save()
      return redirect('tasks')
  #si es post actualizara la tarea y le mostrara la fecha
  #si tiene una fecha es porque ya se cumplio esa tarea
  #lo re direccionara a la vista de tareas
  
@login_required
def delete_task(request,task_id):
  task =  get_object_or_404(Task, pk=task_id, user=request.user )
  if request.method == 'POST':
      task.delete()
      return redirect('tasks')

@login_required               
def signout(request):
    logout(request)
    return redirect('home')

def signin(request):
    if request.method == 'GET':
        return render(request,'signin.html',{
        'form' : AuthenticationForm
    })
        #envia el formulario
    else:
      user =  authenticate(request, username=request.POST['username'], password=request.POST['password'])
      if user is None:
              return render(request,'signin.html',{
                'form' : AuthenticationForm,
                'error': 'usuario es incorrecto pai'
    })
              #si el usuario no existe se envia mensaje de error
      else:
          login(request,user)
          return redirect('tasks')
      #si user es correcto lo enviara al apartado de tareas y guardaras la sesion
      
          

   
        
        