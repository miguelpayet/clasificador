from abc import ABC, abstractmethod
from datetime import date


class Campo(ABC):
    
    def __init__(self, nombre, valor):
        self.nombre = nombre
        self.valor = valor
        
    def valor_sql(self):
        return self.valor


class CampoFecha(Campo):

    def valor_sql(self):
        if isinstance(self.valor, date):
            return self.valor
        return self.valor.date()


class CampoNumero(Campo):
    
    def valor_sql(self):
        if self.valor is not None:
            if self.valor.strip() == '':
                return 0
            else:
                return float(self.valor.replace(",", ""))
        return None
