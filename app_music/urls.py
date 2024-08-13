from django.urls import path
from app_music import views

urlpatterns = [
    path('', views.inicio, name ="Inicio"),
    path('cursos/', views.cursos, name ="Cursos"),
    path('profesores/', views.profesores, name ="Profesores"),
    path('estudiantes/', views.estudiantes, name ="Estudiantes"),
    path('form_curso/', views.form_curso, name="Form_Curso"),
    path('form_estudiante/', views.form_estudiante, name="Form_Estudiante"),
    path('form_profesor/', views.form_profesor, name="Form_Profesor"),
    path('buscar_curso/', views.buscar_curso, name="Buscar_Curso"),
    path('estudiantes/listar', views.EstudianteListView.as_view(), name ="ListarEstudiantes"),
    path('estudiantes/<pk>/borrar', views.EstudianteDeleteView.as_view(), name ="EstudianteBorrar"),
    path('estudiantes/<pk>/actualiza', views.EstudianteUpdateView.as_view(), name ="ActualizaEstudiante"),
]