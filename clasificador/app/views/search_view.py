from app.views.consulta_view import ConsultaView
from django.db import connection
from django.http import JsonResponse
import json


class SearchView(ConsultaView):

    def get_gastos_yape(self, cuenta, mes, año):
        sql_movimiento = self.get_query('detalle_cuenta.sql')
        print(sql_movimiento)
        print('%Pago YAPE%', cuenta, mes, año)
        return self.get_consulta(sql_movimiento, ['%Pago YAPE%', cuenta, mes, año])

    def obtenerDatos(self, post):
        return self.get_gastos_yape(post.get('cuenta'), post.get('mes'), post.get('año'))
