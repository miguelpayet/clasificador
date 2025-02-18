from grabador import Grabador
from seccion import Seccion
import re
from eecc import EECC


class EECCCreditoVisa(EECC):

    def __init__(self):
        self.nombre = 'Estado de Cuenta Tarjeta VISA'
        self.cuenta = 'Visa'
        self.regex_fecha = r'(\d{2})\/(\d{2})\/(\d{2})\s+(\d{2})\/(\d{2})\/(\d{2})'
        super().__init__()

    def add_seccion_linea(self):
        seccion = Seccion()
        seccion.set_regex(
            r'(\d{2}(?:Ene|Feb|Mar|Abr|May|Jun|Jul|Ago|Set|Oct|Nov|Dic))\s+(\d{2}(?:Ene|Feb|Mar|Abr|May|Jun|Jul|Ago|Set|Oct|Nov|Dic))\s+(.*)\s(\d{1,3}(,\d{3})*(\.\d+)?)')
        seccion.add_texto_fijo('cuenta', self.cuenta)
        seccion.add_texto_fecha('fecha_consumo', 0, 5,
                                self.fecha_inicio, self.fecha_fin)
        seccion.add_texto_fecha('fecha_proceso', 9, 5,
                                self.fecha_inicio, self.fecha_fin)
        seccion.add_texto('descripcion', 18, 23)
        seccion.add_texto('ciudad', 41, 13)
        seccion.add_texto('pais', 55, 3)
        seccion.add_texto('tipo', 73, 8)
        seccion.add_numero_especial(86, 10, 'PEN')
        seccion.add_numero_especial(96, 12, 'USD')
        self.secciones.append(seccion)

    def add_seccion_saldo(self):
        self.add_seccion_saldo_soles()
        self.add_seccion_saldo_dolares()

    def add_seccion_saldo_soles(self):
        seccion = Seccion()
        seccion.set_regex(r'(SALDO ANTERIOR)\s+(\d{1,3}(,\d{3})*(\.\d+)?)')
        seccion.add_texto_fijo('cuenta', self.cuenta)
        seccion.add_fecha_fija('fecha_proceso', self.fecha_inicio)
        seccion.add_fecha_fija('fecha_consumo', self.fecha_inicio)
        seccion.add_texto('descripcion', 0, 23)
        seccion.add_numero_especial(67, 10, 'PEN')
        self.secciones.append(seccion)

    def add_seccion_saldo_dolares(self):
        seccion = Seccion()
        seccion.set_regex(r'(SALDO ANTERIOR)\s+(\d{1,3}(,\d{3})*(\.\d+)?)')
        seccion.add_texto_fijo('cuenta', self.cuenta)
        seccion.add_fecha_fija('fecha_proceso', self.fecha_inicio)
        seccion.add_fecha_fija('fecha_consumo', self.fecha_inicio)
        seccion.add_texto('descripcion', 0, 23)
        seccion.add_numero_especial(79, 10, 'USD')
        self.secciones.append(seccion)
