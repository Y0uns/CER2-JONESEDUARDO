from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class TIPO_CHOICES(models.TextChoices):
    SUS_ACTIVIDADES = "S",("Suspension de actividades")
    SUS_CLASES = "C", ("Suspension de clases")
    INFO = "I", ("Informacion")

class Entidad(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=50, null=True)
    logo = models.ImageField(upload_to="Logos Entidad", null=True)
    def __str__(self) -> str:
        return self.nombre

class Comunicado(models.Model):
    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=50, null=True)
    detalle = models.CharField(max_length=50, null=True)
    tipo = models.CharField(max_length=1,
        choices=TIPO_CHOICES.choices,
        default=TIPO_CHOICES.SUS_ACTIVIDADES)
    entidad = models.ForeignKey(Entidad, on_delete=models.CASCADE)
    visible = models.BooleanField(default=True)
    fecha_publicacion = models.DateTimeField(default=timezone.now)
    fecha_ultima_modificacion = models.DateTimeField(default=timezone.now)
    publicado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comunicados_publicados', null=True)
    modificado_por = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comunicados_modificados', null=True)
