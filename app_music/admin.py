from django.contrib import admin
from .models import Profesor, Estudiante, Curso

# Register your models here.
admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Profesor)
