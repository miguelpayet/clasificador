from app.views.ajax_view import AjaxView
from django.db import connection
from django.http import JsonResponse
import json


class SearchView(AjaxView):

    def get_gastos_yape(self, year, month):
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT g.id, g.fecha_proceso, g.descripcion, coalesce(y.nombre, '') yapero, g.moneda, g.debe, g.haber , g.idclase
                FROM gasto g LEFT OUTER JOIN yapero y ON (g.descripcion LIKE %s AND SUBSTRING(g.descripcion, 13, 6) = y.numero)
                WHERE g.cuenta = %s AND EXTRACT(MONTH FROM g.fecha_proceso) = %s AND EXTRACT(YEAR FROM g.fecha_proceso) = %s
            """, ['%YAPE%', 'Ahorro', month, year])
            return json.dumps(
                [dict(zip([col[0] for col in cursor.description], row))
                 for row in cursor.fetchall()],
                default=str
            )

    def obtenerDatos(self, unaClase, unMes, unAño):
        return self.get_gastos_yape(unAño, unMes)

    def post(self, request, *args, **kwargs):
        if self.is_ajax(request):
            post = request.POST
            datos = self.obtenerDatos(post.get('clase'),
                                      post.get('mes'), post.get('año'))
            data = {"registros": datos}
            return JsonResponse(data, status=200)
        else:
            return self.RespuestaNoPermitida()
