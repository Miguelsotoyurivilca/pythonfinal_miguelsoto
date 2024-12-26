from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.contrib.auth import authenticate, login, logout

from .models import Curso, Trainer, Estudiante
from .forms import CursoFormulario, EstudianteFormulario, TrainerFormulario

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User

# Inicio
def inicio(request):
    return render(request, 'app_proyecto/index.html')

# Cursos
def cursos(request):
    query = request.GET.get("q")
    if query:
        cursos = Curso.objects.filter(nombre__icontains=query) | Curso.objects.filter(comision__icontains=query)
    else:
        cursos = Curso.objects.all()
    return render(request, "app_proyecto/cursos.html", {"cursos":cursos})

@login_required
def detalle_curso_view(request, id):
    curso = Curso.objects.get(id=id)
    return render(request, "app_proyecto/detalle-curso.html", {"curso": curso})

@login_required
def formulario_curso_api(request):
    
    if request.method == "POST":
        curso_form = CursoFormulario(request.POST)

        if curso_form.is_valid():
            info_limpia = curso_form.cleaned_data
            curso = Curso(nombre=info_limpia["nombre"],comision=info_limpia["comision"])
            curso.save()
            return redirect("cursos")
    else:
        curso_form = CursoFormulario()

    contexto = {"form": curso_form}

    return render(request, "app_proyecto/forms/curso-formulario.html", contexto)

@login_required
def editar_curso(request, id):
    curso = get_object_or_404(Curso, id=id)
    
    if request.method == "POST":
        curso_form = CursoFormulario(request.POST, instance=curso) 
        if curso_form.is_valid(): 
            curso_form.save() 
        return redirect("cursos") 
    else: 
        curso_form = CursoFormulario(instance=curso) 
        return render(request, "app_proyecto/editar-curso.html", {"form": curso_form})

@login_required
def eliminar_curso(request, id):
    curso = Curso.objects.get(id=id)
    curso.delete()
    return redirect("cursos")

# students

def students(request):
    query = request.GET.get("q")
    if query:
        estudiantes = Estudiante.objects.filter(nombre__icontains=query) | \
                     Estudiante.objects.filter(apellido__icontains=query)
    else:
        estudiantes = Estudiante.objects.all()
    return render(request, "app_proyecto/students.html", {"estudiantes": estudiantes})

@login_required
def formulario_students(request):
    if request.method == "POST":
        estudiante_form = EstudianteFormulario(request.POST)
        if estudiante_form.is_valid():
            estudiante_form.save()  # Guardar directamente desde el formulario
            return redirect("students")
    else:
        estudiante_form = EstudianteFormulario()
    
    contexto = {"form": estudiante_form}
    return render(request, "app_proyecto/forms/students-formulario.html", contexto)

@login_required
def eliminar_students_view(request, id):
    estudiante = Estudiante.objects.get(id=id)
    estudiante.delete()
    return redirect("students")

@login_required
def editar_students_view(request, id):
    estudiante = get_object_or_404(Estudiante, id=id)
    
    if request.method == "POST":
        estudiante_form = EstudianteFormulario(request.POST, instance=estudiante) 
        if estudiante_form.is_valid(): 
            estudiante_form.save() 
        return redirect("students") 
    else: 
        estudiante_form = EstudianteFormulario(instance=estudiante) 
        return render(request, "app_proyecto/editar-students.html", {"form": estudiante_form})

@login_required
def detalle_students_view(request, id):
    estudiante = Estudiante.objects.get(id=id)
    return render(request, "app_proyecto/detalle-students.html", {"estudiante": estudiante})


# Trainer
def trainer(request):
    trainers = Trainer.objects.all()
    return render(request, "app_proyecto/trainer.html", {"trainers": trainers})

@login_required
def formulario_trainer(request):
    if request.method == "POST":
        trainer_form = TrainerFormulario(request.POST)
        if trainer_form.is_valid():
            trainer_form.save()
            return redirect("trainer")
        else:
            trainer_form = TrainerFormulario()
            return render(request, "app_proyecto/forms/trainer-formulario.html", {"form": trainer_form})
    
    # Handle GET request
    trainer_form = TrainerFormulario()
    return render(request, "app_proyecto/forms/trainer-formulario.html", {"form": trainer_form})

@login_required
def eliminar_trainer(request, id):   
    trainer = Trainer.objects.get(id=id)
    trainer.delete()
    return redirect("trainer")

@login_required
def editar_trainer(request, id):   
    trainer = Trainer.objects.get(id=id)
    
    if request.method == "POST":
        trainer_form = TrainerFormulario(request.POST)
        if trainer_form.is_valid():
            info_limpia = trainer_form.cleaned_data
            trainer.nombre = info_limpia["nombre"]
            trainer.apellido = info_limpia["apellido"]
            trainer.email = info_limpia["email"]
            trainer.profesion = info_limpia["profesion"]
            trainer.save()
            return redirect("trainer")
    else:
        trainer_form = TrainerFormulario(initial={
            "nombre": trainer.nombre,
            "apellido": trainer.apellido,
            "email": trainer.email,
            "profesion": trainer.profesion
        })
    return render(request, "app_proyecto/editar-trainer.html", {"form": trainer_form})

@login_required
def detalle_trainer_view(request, id):    
    trainer = Trainer.objects.get(id=id)
    return render(request, "app_proyecto/detalle-trainer.html", {"trainer": trainer})

# About
def about(request):
    return render(request, 'app_proyecto/about.html')

# LOGIN
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('index') 
        else:
            return redirect('index')
    return render(request, 'app_proyecto/login.html')

# LOGOUT
def user_logout(request):
    logout(request)
    return redirect("login")

# Register
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()  # Crea el usuario
            return redirect("login")
    else:
        form = UserCreationForm()
        # for field in form.fields.values():
        #     print(field.help_text)
        #     field.help_text = None
    return render(request, "app_proyecto/register.html", {"form": form})




