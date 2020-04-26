from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
from core.models import Evento

# def index(request):
#     return redirect('/agenda/')

def login_user(request):
    return render(request, 'login.html')

def eventos(request, titulo):
    evento = Evento.objects.get(titulo=titulo)

    return HttpResponse('<h4>Evento: {} Local: {}</h4>'.format(evento.descricao, evento.local))

@login_required(login_url='/login/')
def lista_eventos(request):
    usuario = request.user
    eventos = Evento.objects.filter(usuario=usuario)
    # eventos = Evento.objects.all()
    dados = {'eventos': eventos}

    return render(request, 'agenda.html', dados)

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        usuario = authenticate(username=username, password=password)

        if usuario is not None:
            login(request, usuario)
            return redirect('/')
        else:
            messages.error(request, 'usuário ou senha inválida')

    return redirect('/')

def logout_user(request):
    logout(request)
    return redirect('/')