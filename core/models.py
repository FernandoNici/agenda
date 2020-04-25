from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Evento(models.Model):
    class Meta:
        db_table = 'evento'

    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField()
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo