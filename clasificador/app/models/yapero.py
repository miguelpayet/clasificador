from django.db import models


class Yapero(models.Model):
    numero = models.TextField(blank=True, primary_key=True)
    nombre = models.TextField(blank=True, null=True)

    class Meta:
        db_table = "yapero"
        verbose_name_plural = "Yaperos"

    def __str__(self):
        return self.nombre if self.nombre else "Yapero sin nombre"
