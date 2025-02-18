from campo import Campo

class Registro:
    
    def __init__(self):
        self.campos = []
        
    def add_campo(self, campo):
        self.campos.append(campo)
        
    def get_tuple(self):
        return tuple(obj.valor_sql() for obj in self.campos)