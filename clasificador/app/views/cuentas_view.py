from app.models.cuenta import Cuenta
from app.views.tabla_base_view import TablaBaseView


class CuentasView(TablaBaseView):
    clase = Cuenta
