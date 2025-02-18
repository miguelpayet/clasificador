import mysql.connector


class Grabador():

    def __init__(self, properties):
        self.coneccion = None
        self.bd = properties.nombrebd
        self.host = properties.hostbd
        self.password = properties.passwordbd
        self.usuario = properties.usuariobd

    def conectar(self):
        self.coneccion = mysql.connector.connect(
            user=self.usuario, password=self.password, host=self.host, database=self.bd)

    def grabar(self, registro):
        campos = ', '.join(campo.nombre for campo in registro.campos)
        placeholders = ', '.join(['%s'] * len(registro.campos))
        sql = f'INSERT INTO gasto ({campos}) VALUES ({placeholders})'
        valores = registro.get_tuple()
        with self.coneccion.cursor() as cursor:
            cursor.execute(sql, valores)
        self.coneccion.commit()
