from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from core.models import Evento


def eventos(request, titulo):
    evento = Evento.objects.get(titulo=titulo)

    return HttpResponse('<h4>Evento: {} Local: {}</h4>'.format(evento.descricao, evento.local))