from app.views.form_view import FormView


class PaginaIndexView(FormView):
    template_name = "index.html"
    url_string = 'search'
