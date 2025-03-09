from app.models.cuenta import Cuenta
from app.views.consulta_view import ConsultaView


class ResumenAhorroView(ConsultaView):

    def get_resumen_ahorros(self, id, mes, año):
        query = self.get_query('resumen_ahorro.sql')
        return self.get_consulta(query, ['%Pago YAPE%', id, mes, año])

    def obtenerDatos(self, post):
        id = Cuenta.objects.get(nombre='Ahorro').id
        return self.get_resumen_ahorros(id, post.get('mes'), post.get('año'))
