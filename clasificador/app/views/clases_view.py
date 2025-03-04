from app.views.tabla_base_view import TablaBaseView
from app.views.ajax_view import AjaxView
from app.models.clase import Clase


class ClasesView(TablaBaseView):
    clase = Clase
