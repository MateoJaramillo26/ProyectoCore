from django.urls import path
from . import views

app_name = 'academico'

urlpatterns = [
    # Rutas para profesores
    path('profesor/dashboard/', views.profesor_dashboard, name='profesor_dashboard'),
    path('profesor/calificacion/crear/', views.crear_calificacion, name='crear_calificacion'),
    path('profesor/calificacion/<int:calificacion_id>/actualizar/', views.actualizar_calificacion, name='actualizar_calificacion'),
    
    # Rutas para estudiantes
    path('estudiante/dashboard/', views.estudiante_dashboard, name='estudiante_dashboard'),
    path('estudiante/calificaciones/', views.ver_calificaciones, name='ver_calificaciones'),
    
    # Rutas compartidas
    path('universidades/', views.ver_universidades, name='ver_universidades'),
]