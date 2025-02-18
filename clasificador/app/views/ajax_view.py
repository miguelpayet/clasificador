from django.http import JsonResponse
from django.views import View


class AjaxView(View):

    def is_ajax(self, request):
        return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

    def RespuestaNoPermitida(self):
        return JsonResponse({"error": "Solo solicitudes AJAX son permitidas"}, status=400)
