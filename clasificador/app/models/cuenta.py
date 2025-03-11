from django.db import models


class Cuenta(models.Model):
    id = models.IntegerField(blank=True, primary_key=True)
    nombre = models.CharField(blank=True, max_length=30, null=True)
    orden = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = "cuenta"
        verbose_name_plural = "cuentas"

    def __str__(self):
        return self.nombre if self.nombre else "Cuenta sin nombre"
