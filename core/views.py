from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from core.models import Evento

# def index(request):
#     return redirect('/agenda/')



def eventos(request, titulo):
    evento = Evento.objects.get(titulo=titulo)

    return HttpResponse('<h4>Evento: {} Local: {}</h4>'.format(evento.descricao, evento.local))

def lista_eventos(request):
    # usuario = request.user
    # eventos = Evento.objects.get(usuario=usuario)
    eventos = Evento.objects.all()
    dados = {'eventos': eventos}

    return render(request, 'agenda.html', dados)