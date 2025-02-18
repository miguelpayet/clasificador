import re
from datetime import date
from grabador import Grabador

class EECC:

    def __init__(self):
        self.fecha_fin = None
        self.fecha_inicio = None
        self.registros = []
        self.secciones = []
        self.nombre = None
        self.regex_fecha = ''

    def add_seccion_linea(self):
        pass

    def add_seccion_saldo(self):
        pass

    def es_lector(self, texto):
        return self.nombre in texto

    def extraer_fecha(self, text):
        res = self.pattern_fecha.search(text)
        if res:
            dia_inicio = int(res.group(1))
            mes_inicio = int(res.group(2))
            año_inicio = 2000 + int(res.group(3))
            self.fecha_inicio = date(año_inicio, mes_inicio, dia_inicio)
            dia_fin = int(res.group(4))
            mes_fin = int(res.group(5))
            año_fin = 2000 + int(res.group(6))
            self.fecha_fin = date(año_fin, mes_fin, dia_fin)

    def grabar(self, properties):
        grabador = Grabador(properties)
        grabador.conectar()
        for registro in self.registros:
            grabador.grabar(registro)

    def inicializar(self, texto):
        self.pattern_fecha = re.compile(self.regex_fecha)
        self.extraer_fecha(texto)
        self.add_seccion_saldo()
        self.add_seccion_linea()

    def leer_tabla(self, tabla):
        lineas = tabla.data[1][1].split('\n')
        for linea in lineas:
            for seccion in self.secciones:
                if seccion.es_para_linea(linea):
                    registro = seccion.procesar_linea(linea)
                    self.registros.append(registro)
