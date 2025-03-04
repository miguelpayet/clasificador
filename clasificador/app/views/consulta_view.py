from app.views import ajax_view
from django.db import connection
from django.http import JsonResponse
import json


class ConsultaView(ajax_view.AjaxView):

    def get_consulta(self, sql, params):
        with connection.cursor() as cursor:
            cursor.execute(sql, params)
            return json.dumps(
                [dict(zip([col[0] for col in cursor.description], row))
                 for row in cursor.fetchall()],
                default=str
            )

    def post(self, request, *args, **kwargs):
        if self.is_ajax(request):
            post = request.POST
            datos = self.obtenerDatos(post.get('clase'),
                                      post.get('mes'), post.get('año'))
            data = {"registros": datos}
            return JsonResponse(data, status=200)
        else:
            return self.RespuestaNoPermitida()
