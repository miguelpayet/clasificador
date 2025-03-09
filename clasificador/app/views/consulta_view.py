from app.views import ajax_view
from django.conf import settings
from django.db import connection
from django.http import JsonResponse
import json
import os


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
            datos = self.obtenerDatos(request.POST)
            data = {"registros": datos}
            return JsonResponse(data, status=200)
        else:
            return self.RespuestaNoPermitida()

    def get_query(self, archivo):
        static_dir = settings.STATICFILES_DIRS[0]
        query = ""
        with open(os.path.join(static_dir, 'sql', archivo), 'r', encoding='utf-8') as archivo:
            query = archivo.read()
        return query
