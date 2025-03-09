from seccion import Seccion
import re
from eecc import EECC


class EECCAhorro(EECC):

    def __init__(self):
        super().__init__()
        self.nombre = 'Estado de Cuenta de Ahorros CUENTA SUELDO BCP'
        self.cuenta = 'ahorro'
        self.idcuenta = 35
        self.regex_fecha = r'.*DEL\s+(\d{2})/(\d{2})/(\d{2})\s+AL\s+(\d{2})/(\d{2})/(\d{2})\n'

    def add_seccion_linea(self):
        seccion = Seccion()
        seccion.set_regex(
            r'(\d{2}(?:ENE|FEB|MAR|ABR|MAY|JUN|JUL|AGO|SET|OCT|NOV|DIC))\s+(\d{2}(?:ENE|FEB|MAR|ABR|MAY|JUN|JUL|AGO|SET|OCT|NOV|DIC))\s+(.*)\s(\d{1,3}(,\d{3})*(\.\d+)?)')
        seccion.add_texto_fijo('moneda', 'PEN')
        seccion.add_texto_fijo('idcuenta', '35')
        seccion.add_texto_fecha('fecha_proceso', 0, 5,
                                self.fecha_inicio, self.fecha_fin)
        seccion.add_texto_fecha('fecha_consumo', 6, 5,
                                self.fecha_inicio, self.fecha_fin)
        seccion.add_texto('descripcion', 12, 30)
        seccion.add_numero('haber', 44, 10)
        seccion.add_numero('debe', 62, 10)
        self.secciones.append(seccion)

    def add_seccion_saldo(self):
        seccion = Seccion()
        seccion.add_texto_fijo('moneda', 'PEN')
        seccion.add_texto_fijo('idcuenta', 35)
        seccion.set_regex(r'(SALDO ANTERIOR)\s+(\d{1,3}(,\d{3})*(\.\d+)?)')
        seccion.add_fecha_fija('fecha_proceso', self.fecha_inicio)
        seccion.add_fecha_fija('fecha_consumo', self.fecha_inicio)
        seccion.add_texto('descripcion', 0, 14)
        seccion.add_numero('haber', 53, 10)
        self.secciones.append(seccion)
