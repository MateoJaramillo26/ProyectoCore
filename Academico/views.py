from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Clase, Calificacion, Universidad, Ciudad, Pais
from django.core.exceptions import PermissionDenied

def is_profesor(user):
    return user.is_authenticated and user.role == 'profesor'

def is_estudiante(user):
    return user.is_authenticated and user.role == 'estudiante'

# Vistas para Profesores
@login_required
@user_passes_test(is_profesor)
def profesor_dashboard(request):
    clases = Clase.objects.filter(profesor=request.user)
    return render(request, 'academico/profesor/dashboard.html', {'clases': clases})

@login_required
@user_passes_test(is_profesor)
@require_http_methods(["POST"])
def crear_calificacion(request):
    # Lógica para crear calificación
    if request.method == 'POST':
        estudiante_id = request.POST.get('estudiante')
        clase_id = request.POST.get('clase')
        nota = request.POST.get('nota')
        comentario = request.POST.get('comentario')
        
        clase = get_object_or_404(Clase, id_clase=clase_id, profesor=request.user)
        calificacion = Calificacion.objects.create(
            estudiante_id=estudiante_id,
            clase=clase,
            nota=nota,
            comentario=comentario
        )
        return JsonResponse({'status': 'success'})

@login_required
@user_passes_test(is_profesor)
@require_http_methods(["PUT"])
def actualizar_calificacion(request, calificacion_id):
    calificacion = get_object_or_404(Calificacion, id_calificacion=calificacion_id)
    if calificacion.clase.profesor != request.user:
        raise PermissionDenied
    
    # Actualizar calificación
    nota = request.POST.get('nota')
    comentario = request.POST.get('comentario')
    calificacion.nota = nota
    calificacion.comentario = comentario
    calificacion.save()
    return JsonResponse({'status': 'success'})

# Vistas para Estudiantes
@login_required
@user_passes_test(is_estudiante)
def estudiante_dashboard(request):
    calificaciones = Calificacion.objects.filter(estudiante=request.user)
    return render(request, 'academico/estudiante/dashboard.html', {'calificaciones': calificaciones})

@login_required
@user_passes_test(is_estudiante)
def ver_calificaciones(request):
    calificaciones = Calificacion.objects.filter(estudiante=request.user)
    return render(request, 'academico/estudiante/calificaciones.html', {'calificaciones': calificaciones})

# Vistas compartidas (requieren autenticación)
@login_required
def ver_universidades(request):
    universidades = Universidad.objects.all()
    return render(request, 'academico/universidades.html', {'universidades': universidades})
