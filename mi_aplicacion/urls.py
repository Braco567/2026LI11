from django.urls import path
from mi_aplicacion.views import Home, Escuelas, EscuelaAlta, EscuelaEditar, EscuelaEliminar, Maestros,MaestroAlta,MaestroEliminar,MaestroEditar, AlumnoAlta, Alumnos, AlumnoEditar, AlumnoEliminar

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('escuelas', Escuelas.as_view(), name='escuelas'),
    path('escuelas_alta', EscuelaAlta.as_view(), name='escuelas_alta'),
    path('escuelas_editar/<int:id>', EscuelaEditar.as_view(), name='escuelas_editar'),
    path('escuelas_eliminar/<int:id>', EscuelaEliminar.as_view(), name='escuelas_eliminar'),
    path('maestros', Maestros.as_view(), name='maestros'),
    path('maestros_alta', MaestroAlta.as_view(), name='maestros_alta'),
    path('maestros_eliminar/<int:id>', MaestroEliminar.as_view(), name='maestros_eliminar'),
    path('maestros_editar/<int:id>', MaestroEditar.as_view(), name='maestros_editar'),
    path('alumnos', Alumnos.as_view(), name='alumnos'),
    path('alumnos_alta', AlumnoAlta.as_view(), name='alumnos_alta'),
    path('alumnos_editar/<int:id>', AlumnoEditar.as_view(), name='alumnos_editar'),
    path('alumnos_eliminar/<int:id>', AlumnoEliminar.as_view(), name='alumnos_eliminar'),
]
    


