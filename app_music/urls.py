from django.urls import path
from app_music import views


urlpatterns = [
    path('', views.inicio, name ="Inicio"),
    path('cursos/', views.cursos, name ="Cursos"),
    path('profesores/', views.profesores, name ="Profesores"),
    path('form_curso/', views.form_curso, name="Form_Curso"),
    path('form_profesor/', views.form_profesor, name="Form_Profesor"),
    path('buscar_curso/', views.buscar_curso, name="Buscar_Curso"),
    path('estudiantes/listar', views.EstudianteListView.as_view(), name ="ListarEstudiantes"),
    path('estudiantes/nuevo', views.EstudianteCreateView.as_view(), name ="NuevoEstudiante"),
    path('estudiantes/<pk>/borrar', views.EstudianteDeleteView.as_view(), name ="EstudianteBorrar"),
    path('estudiantes/<pk>/actualiza', views.EstudianteUpdateView.as_view(), name ="ActualizaEstudiante"),
    path('estudiantes/<pk>/detalle', views.EstudianteDetailView.as_view(), name ="EstudianteDetalle"),
    path('cursos/listar', views.CursoListView.as_view(), name ="ListarCursos"),
    path('cursos/nuevo', views.CursoCreateView.as_view(), name ="NuevoCurso"),
    path('cursos/<pk>/borrar', views.CursoDeleteView.as_view(), name ="CursoBorrar"),
    path('cursos/<pk>/actualiza', views.CursoUpdateView.as_view(), name ="ActualizaCurso"),
    path('cursos/<pk>/detalle', views.CursoDetailView.as_view(), name ="CursoDetalle"),
    path('about/', views.about, name ="About"),
]