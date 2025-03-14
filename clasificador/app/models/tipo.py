from django.db import models


class Tipo(models.Model):
    id = models.AutoField(primary_key=True)
    incluir = models.BooleanField(default=True)
    nombre = models.CharField(max_length=30, null=True, blank=True)
    orden = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'tipo'
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'

    def __str__(self):
        return self.nombre or 'Sin nombre'
