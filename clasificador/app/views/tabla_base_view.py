from app.views.ajax_view import AjaxView
from django.db import connection
from django.forms.models import model_to_dict
from django.http import JsonResponse
import json


class TablaBaseView(AjaxView):

    def obtenerDatos(self):
        queryset = self.clase.objects.order_by('nombre').all()
        json = [model_to_dict(obj) for obj in queryset]
        return json

    def get(self, request, *args, **kwargs):
        if self.is_ajax(request):
            datos = self.obtenerDatos()
            data = {"registros": datos}
            return JsonResponse(data, status=200)
        else:
            return self.RespuestaNoPermitida()
