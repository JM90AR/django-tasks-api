from django.db import models
from django.contrib.auth.models import User

class Tarea(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    completada = models.BooleanField(default=False)
    creada = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tareas")

    def __str__(self):
        return self.titulo