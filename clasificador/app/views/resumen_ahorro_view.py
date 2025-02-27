from app.views.consulta_view import ConsultaView
from django.conf import settings
import os


class ResumenAhorroView(ConsultaView):

    def get_resumen_ahorros(self, year, month):
        static_dir = settings.STATICFILES_DIRS[0]
        sql_resumen_ahorros = ""
        with open(os.path.join(static_dir, 'sql', 'resumen_ahorro.sql'), 'r', encoding='utf-8') as archivo:
            sql_resumen_ahorros = archivo.read()
        return self.get_consulta(sql_resumen_ahorros, ['%Pago YAPE%', 'Ahorro', month, year])

    def obtenerDatos(self, unaClase, unMes, unAño):
        return self.get_resumen_ahorros(unAño, unMes)
