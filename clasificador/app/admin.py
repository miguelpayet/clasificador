from django.contrib import admin
from .models import Clase
from .models import Yapero


@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)
    list_filter = ('nombre',)
    ordering = ('nombre',)


@admin.register(Yapero)
class YaperoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'nombre')
    search_fields = ('numero', 'nombre')
    list_filter = ('numero', 'nombre')
    ordering = ('nombre',)
