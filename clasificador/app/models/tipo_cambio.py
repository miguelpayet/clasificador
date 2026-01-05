from django.db import models


class TipoCambio(models.Model):
    id = models.AutoField(primary_key=True)
    año = models.IntegerField(null=True, blank=True)
    mes = models.IntegerField(null=True, blank=True)
    tipo_cambio = models.FloatField(null=True, blank=True)

    class Meta:
        db_table = 'tipocambio'
        verbose_name = 'Tipo de cambio'
        verbose_name_plural = 'Tipos de cambio'

    def __str__(self):
        return f"Tipo de cambio mes: {self.mes} año: {self.año}"
