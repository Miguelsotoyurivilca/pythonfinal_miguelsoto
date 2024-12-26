from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from .models import Trainer, Curso, Estudiante

class CursoFormulario(forms.ModelForm):
    
    class Meta:
        model = Curso
        fields = "__all__"
        labels = { 
            'nombre': '',
            'comision': '',
            'descripcion': '',
            'imagen': '',
        }
        widgets = {
            "nombre": forms.TextInput(attrs={ 
                "class":"form-control", "placeholder":"Ingrese el nombre del curso"
            },),
            "comision":forms.NumberInput(attrs={
                "class":"form-control", "placeholder":"Ingrese el numero de comision"
            }),
            "descripcion": forms.Textarea(attrs={
                "class":"form-control", "placeholder":"Ingrese la descripcion del curso"
            })
        }

class EstudianteFormulario(forms.ModelForm):
    
    class Meta:
        model = Estudiante
        fields = "__all__"
        
        widgets = {
            "nombre": forms.TextInput(attrs={
                "class":"form-control", "placeholder":"Ingrese el nombre"
            },),
            "apellido": forms.TextInput(attrs={
                "class":"form-control", "placeholder":"Ingrese el apellido"
            },),
            "email": forms.EmailInput(attrs={
                "class":"form-control", "placeholder":"Ingrese el Correo electónico"
            },),
        }

class TrainerFormulario(forms.ModelForm):
    
    class Meta:
        model = Trainer
        fields = "__all__"
        
        widgets = {
            "nombre": forms.TextInput(attrs={
                "class":"form-control", "placeholder":"Ingrese el nombre"
            },),
            "apellido": forms.TextInput(attrs={
                "class":"form-control", "placeholder":"Ingrese el apellido"
            },),
            "email": forms.EmailInput(attrs={
                "class":"form-control", "placeholder":"Ingrese el Correo electónico"
            },),
            "profesion": forms.TextInput(attrs={
                "class":"form-control", "placeholder":"Ingrese la profesion"
            },),
        }
