from django.contrib import admin
from .models import Curso, Trainer, Estudiante

# Register your models here.
admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Trainer)