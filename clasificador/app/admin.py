from .models import Clase
from .models import Cuenta
from .models import Gasto
from .models import Yapero
from django.contrib import admin


@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ('nombre',)
    list_filter = ('nombre',)
    ordering = ('nombre',)


@admin.register(Cuenta)
class CuentaAdmin(admin.ModelAdmin):
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


@admin.register(Gasto)
class GastoAdmin(admin.ModelAdmin):
    list_display = ('cuenta', 'fecha_consumo', 'descripcion', 'moneda', 'debe', 'haber')
    list_filter = ('clase', 'cuenta', 'moneda', 'fecha_consumo')
    search_fields = ('descripcion', 'ciudad', 'tipo')
    ordering = ('fecha_proceso',)
    fields = ('clase', 'cuenta', 'descripcion', 'fecha_consumo', 'fecha_proceso',
              'moneda', 'debe', 'haber', 'ciudad', 'pais', 'tipo')
