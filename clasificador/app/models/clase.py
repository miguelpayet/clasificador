from django.db import models


class Clase(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30, null=True, blank=True)
    orden = models.IntegerField(null=True, blank=True)
    tipo = models.ForeignKey('Tipo', models.DO_NOTHING, db_column='idtipo', blank=True, null=True)

    class Meta:
        db_table = 'clase'
        verbose_name = 'Clase'
        verbose_name_plural = 'Clases'

    def __str__(self):
        return self.nombre or 'Sin nombre'
