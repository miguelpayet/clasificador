from columna import *
from registro import Registro
import re


class Seccion:

    def __init__(self):
        self.regex = ''
        self.columnas = []

    def add_fecha_fija(self, nombre, valor):
        col = ColumnaFechaFija(nombre, valor)
        self.columnas.append(col)

    def add_numero(self, nombre, posicion, longitud):
        col = ColumnaNumero(nombre, posicion, longitud)
        self.columnas.append(col)

    def add_numero_especial(self, posicion, longitud, moneda):
        col = ColumnaNumeroEspecial(posicion, longitud, moneda)
        self.columnas.append(col)

    def add_texto(self, nombre, posicion, longitud):
        col = Columna(nombre, posicion, longitud)
        self.columnas.append(col)

    def add_texto_fijo(self, nombre, valor):
        col = ColumnaTextoFijo(nombre, valor)
        self.columnas.append(col)

    def add_texto_fecha(self, nombre, posicion, longitud, fecha_inicio, fecha_fin):
        col = ColumnaTextoFecha(nombre, posicion, longitud)
        col.fecha_inicio = fecha_inicio
        col.fecha_fin = fecha_fin
        self.columnas.append(col)

    def es_para_linea(self, linea):
        self.result = self.pattern.search(linea)
        return self.result is not None

    def procesar_linea(self, linea):
        registro = Registro()
        linea = linea.lstrip()
        for columna in self.columnas:
            columna.agregar_valor(linea, registro)
        return registro

    def set_regex(self, regex):
        self.regex = regex
        self.pattern = re.compile(regex)
