class Properties():
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.leer_archivo()
        
    def leer_archivo(self):
        f = open(self.nombre)
        for linea in f:
            arreglo = linea.rstrip().split(":")
            setattr(self, arreglo[0], arreglo[1].strip())
            
properties = Properties('gastos.properties')
