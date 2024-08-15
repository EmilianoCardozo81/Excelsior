# Exelsior
Mi nombre es Emiliano Cardozo.
En este proyecto intente reproducir todo lo visto en el curso.
Genere dos aplicaciones. 
Una contiene la funcionalidad principal (app_music), donde figuran las vistas de y las urls. 
En la otra (users) figura todo lo relacionado con el usuario (CRUD).

### Detalle de lo armado en esta entrega:
Cree el superusuario: Test con la clave: 123

También agregue un usuario (Emiliano) que solo pueda visualizar que solo puede visualizar los cursos existentes.

**Tengo la idea se armar una página para una escuela de música.**
## Arme las  siguientes urls según lo visto en clase:
```python
1.    path('', views.inicio, name ="Inicio"),
2.    path('cursos/', views.cursos, name ="Cursos"),
3.    path('profesores/', views.profesores, name ="Profesores"),
4.    path('buscar_curso/', views.buscar_curso, name="Buscar_Curso"),
5.    path('about/', views.about, name ="About"),
6.    path('cursos/listar', views.CursoListView.as_view(), name ="ListarCursos"),
7.    path('estudiantes/listar', views.EstudianteListView.as_view(), name ="ListarEstudiantes"),
```
## Agregue los siguientes formularios:
```python
1.    path('cursos/listar', views.CursoListView.as_view(), name ="ListarCursos"), #El cual se utiliza para agregar cursos a la base de datos.
2.    path('estudiantes/listar', views.EstudianteListView.as_view(), name ="ListarEstudiantes"), #El cual se utiliza para agregar estudiantes a la base de datos.
3.    path('form_profesor/', views.form_profesor, name="Form_Profesor"), #El cual se utiliza para agregar profesores a la base de datos.
4.    path('buscar_curso/', views.buscar_curso, name="Buscar_Curso"), #El cual se utiliza para buscar los cursos que figuran en la base de datos.
```

**El proyecto tiene el nombre: excelsior**<br>
**La aplicación tiene el nombre: app_music**

