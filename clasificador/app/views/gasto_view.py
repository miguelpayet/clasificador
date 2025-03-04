from app.models import Clase
from app.models import Gasto
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
import json


class GastoView(View):

    def patch(self, request, *args, **kwargs):
        try:
            id_gasto = kwargs['id']
            gasto = Gasto.objects.get(id=id_gasto)
            data = request.body.decode('utf-8')
            data_dict = json.loads(data)
            for key, value in data_dict.items():
                if key == 'idclase':
                    gasto.clase = Clase.objects.get(id=int(value))
                else:
                    setattr(gasto, key, value)
            gasto.save()
            return JsonResponse({"message": "gasto updated successfully"})
        except Gasto.DoesNotExist:
            return JsonResponse({"error": "gasto not found"}, status=404)
