from django.shortcuts import render
from django.http import HttpResponse
from app_music.models import *
from app_music.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class EstudianteListView(ListView):
    model = Estudiante
    context_object_name ="Estudiantes"
    template_name = "app_music/lista_estudiantes.html"

class EstudianteDeleteView(DeleteView):
    model = Estudiante
    template_name = "app_music/estudiante_borrar.html"
    success_url = reverse_lazy("ListarEstudiantes")

class EstudianteUpdateView(UpdateView):
    model = Estudiante
    template_name = "app_music/estudiante_actualizar.html"
    success_url = reverse_lazy("ListarEstudiantes") 
    fields = ['nombre','apellido']




def inicio(request):
    return render (request, "app_music/index.html")

def cursos(request):
    return render (request, "app_music/cursos.html")

def profesores(request):
    return render (request, "app_music/profesores.html")

def estudiantes(request):
    return render (request, "app_music/estudiantes.html")

def entregables(request):
    return render (request, "app_music/entregables.html")

def form_curso(request):
    if request.method == "POST":
        mi_formulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])
            curso.save()

            return render(request, "app_music/index.html")
    else:
        mi_formulario = CursoFormulario()

    return render(request, "app_music/form_curso.html", {"mi_formulario": mi_formulario})

def form_estudiante(request):
    if request.method == "POST":
        mi_form = EstudianteFormulario(request.POST) 
        if mi_form.is_valid():
            informacion = mi_form.cleaned_data
            
            estudiante = Estudiante(nombre=informacion["nombre"], apellido=informacion["apellido"],email=informacion["email"])
            estudiante.save()

            return render(request, "app_music/index.html")
    else:
        mi_form = EstudianteFormulario()

    return render(request, "app_music/form_estudiante.html", {"mi_form": mi_form})

def buscar_curso(request):
    if request.method == "POST":
        mi_formulario = BuscaCursoForm(request.POST) 

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            cursos = Curso.objects.filter(nombre__icontains=informacion["curso"])

            return render(request, "app_music/mostrar_cursos.html", {"cursos": cursos})
    else:
        mi_formulario = BuscaCursoForm()

    return render(request, "app_music/buscar_curso.html", {"mi_formulario": mi_formulario})
    
def form_profesor(request):
    if request.method == "POST":
        mi_formulario = ProfesorFormulario(request.POST) 
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            
            profesor = Profesor(nombre=informacion["nombre"], apellido=informacion["apellido"],email=informacion["email"])
            profesor.save()

            return render(request, "app_music/index.html")
    else:
        mi_formulario = ProfesorFormulario()

    return render(request, "app_music/form_profesor.html", {"mi_formulario": mi_formulario})