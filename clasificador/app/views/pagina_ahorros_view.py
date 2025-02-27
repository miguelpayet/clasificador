from app.views.form_view import FormView


class PaginaAhorrosView(FormView):
    template_name = "ahorro.html"
    url_string = 'resumen-ahorros'
