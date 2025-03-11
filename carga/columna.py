from campo import *
import datetime
import re


class Columna():

    def __init__(self, nombre, posicion, longitud):
        self.campo = Campo
        self.longitud = longitud
        self.nombre = nombre
        self.posicion = posicion
        self.valor = None

    def agregar_valor(self, linea, registro):
        self.extraer_valor(linea)
        registro.add_campo(self.get_campo())

    def extraer_valor(self, linea):
        self.valor = linea[self.posicion:self.posicion + self.longitud]

    def get_campo(self):
        return self.campo(self.nombre, self.valor)


class ColumnaFechaFija(Columna):

    def __init__(self, nombre, valor):
        super().__init__(nombre, 0, 0)
        self.valor = valor
        self.campo = CampoFecha

    def agregar_valor(self, linea, registro):
        registro.add_campo(self.get_campo())

    def extraer_valor(self, linea):
        pass


class ColumnaNumero(Columna):

    def __init__(self, nombre, posicion, longitud):
        super().__init__(nombre, posicion, longitud)
        self.campo = CampoNumero


class ColumnaNumeroEspecial(ColumnaNumero):

    def __init__(self, posicion, longitud, moneda):
        super().__init__('', posicion, longitud)
        self.moneda = moneda
        self.nombre = ''

    def agregar_valor(self, linea, registro):
        if self.extraer_valor(linea):
            registro.add_campo(self.get_campo())
            otro_nombre = 'debe' if self.nombre == 'haber' else 'haber'
            registro.add_campo(Campo(otro_nombre, 0))
            registro.add_campo(Campo('moneda', self.moneda))

    def extraer_valor(self, linea):
        tiene_valor = True
        self.valor = linea[self.posicion:self.posicion + self.longitud].strip()
        if self.valor == '':
            return False  # self.nombre = 'debe'
        else:
            if self.valor[-1] == "-":
                self.nombre = 'haber'
            else:
                self.nombre = 'debe'
            self.valor = self.valor.replace('-', '')
        return tiene_valor


class ColumnaTextoFecha(Columna):

    meses = {'ENE': 1, 'FEB': 2, 'MAR': 3, 'ABR': 4, 'MAY': 5, 'JUN': 6,
             'JUL': 7, 'AGO': 8, 'SET': 9, 'OCT': 10, 'NOV': 11, 'DIC': 12}
    pattern = r'([0-9]{2})([A-Z|a-z]{3})'

    def __init__(self,  nombre, posicion, longitud):
        super().__init__(nombre, posicion, longitud)

    def extraer_valor(self, linea):
        super().extraer_valor(linea)
        match = re.search(ColumnaTextoFecha.pattern, self.valor.upper())
        if match:
            dia = int(match.group(1))
            mes = ColumnaTextoFecha.meses[match.group(2).upper()]
            año = self.fecha_inicio.year if mes == self.fecha_inicio.month else self.fecha_fin.year
            self.valor = datetime.datetime(año, mes, dia)


class ColumnaTextoFijo(Columna):

    def __init__(self, nombre, valor):
        super().__init__(nombre, 0, 0)
        self.valor = valor

    def agregar_valor(self, linea, registro):
        registro.add_campo(self.get_campo())

    def extraer_valor(self, linea):
        pass
