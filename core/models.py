from datetime import datetime, timedelta

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
    local = models.CharField(max_length=500, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M')

    def get_data_evento_input(self):
        return self.data_evento.strftime('%Y-%m-%dT%H:%M')
    # def __str__(self):
    #     return self.titulo

    def get_evento_atrasado(self):
        return self.data_evento < datetime.now()