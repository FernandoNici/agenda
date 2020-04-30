from django.contrib import admin

# Register your models here.
from core.models import Evento

class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_criacao', 'data_evento')
    list_filter = ('titulo', 'usuario',)

admin.site.register(Evento, EventoAdmin)

