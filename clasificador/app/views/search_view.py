from app.views.consulta_view import ConsultaView
from django.db import connection
from django.http import JsonResponse
import json


class SearchView(ConsultaView):

    def get_gastos_yape(self, year, month):
        sql_movimiento = """
                SELECT g.id, g.fecha_proceso, g.descripcion, coalesce(y.nombre, '') yapero, g.moneda, g.debe, g.haber , g.idclase
                FROM gasto g LEFT OUTER JOIN yapero y ON (g.descripcion LIKE %s AND SUBSTRING(g.descripcion, 13, 6) = y.numero)
                WHERE g.cuenta = %s AND EXTRACT(MONTH FROM g.fecha_proceso) = %s AND EXTRACT(YEAR FROM g.fecha_proceso) = %s
            """
        return self.get_consulta(sql_movimiento, ['%Pago YAPE%', 'Ahorro', month, year])

    def obtenerDatos(self, unaClase, unMes, unAño):
        return self.get_gastos_yape(unAño, unMes)
