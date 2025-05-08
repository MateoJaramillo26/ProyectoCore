from django.db import models

# Create your models here.
class Universidad(models.Model):
    id_universidad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200, verbose_name="Nombre")
    direccion = models.CharField(max_length=200, verbose_name="Dirección")
    ciudad = models.CharField(max_length=100, verbose_name="Ciudad")
    telefono = models.CharField(max_length=15, verbose_name="Teléfono")
    sitio_web = models.URLField(verbose_name="Sitio Web")

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Universidad"
        verbose_name_plural = "Universidades"

class Clase(models.Model):
    id_clase = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    codigo = models.CharField(max_length=20, verbose_name="Código")
    creditos = models.IntegerField(verbose_name="Créditos")
    aula = models.CharField(max_length=50, verbose_name="Aula")
    horario = models.CharField(max_length=100, verbose_name="Horario")
    periodo = models.CharField(max_length=50, verbose_name="Período")
    profesor = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'profesor'})

    def __str__(self):
        return f"{self.codigo} - {self.nombre}"

    class Meta:
        verbose_name = "Clase"
        verbose_name_plural = "Clases"

class Calificacion(models.Model):
    id_calificacion = models.AutoField(primary_key=True)
    estudiante = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 'estudiante'})
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE)
    nota = models.FloatField(verbose_name="Nota")
    fecha_registro = models.DateField(auto_now_add=True, verbose_name="Fecha de Registro")
    comentario = models.TextField(blank=True, null=True, verbose_name="Comentario")

    def __str__(self):
        return f"{self.estudiante.username} - {self.clase.nombre} - {self.nota}"

    class Meta:
        verbose_name = "Calificación"
        verbose_name_plural = "Calificaciones"