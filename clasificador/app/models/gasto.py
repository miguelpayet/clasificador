from django.db import models
from app.models import Clase
from app.models import Cuenta


class Gasto(models.Model):
    ciudad = models.CharField(max_length=15, blank=True, null=True)
    clase = models.ForeignKey(Clase, db_column='idclase', on_delete=models.DO_NOTHING)
    cuenta = models.ForeignKey(Cuenta, db_column='idcuenta', on_delete=models.DO_NOTHING)
    debe = models.FloatField(blank=True, null=True)
    descripcion = models.CharField(max_length=40, blank=True, null=True)
    fecha_consumo = models.DateField(blank=True, null=True)
    fecha_proceso = models.DateField(blank=True, null=True)
    haber = models.FloatField(blank=True, null=True)
    id = models.AutoField(primary_key=True)
    moneda = models.CharField(max_length=3, blank=True, null=True)
    pais = models.CharField(max_length=3, blank=True, null=True)
    tipo = models.CharField(max_length=10, blank=True, null=True)

    class Meta:
        db_table = "gasto"
        verbose_name_plural = "Gastos"

    def __str__(self):
        return f"{self.descripcion} ({self.fecha_proceso})"
