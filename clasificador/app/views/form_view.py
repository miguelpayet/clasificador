from app.forms.filter_form import FilterForm
from django import forms
from django.template.response import TemplateResponse
from django.views.generic import View
from django.urls import reverse


class FormView(View):
    form_class = FilterForm

    def crear_form(self):
        return self.form_class()

    def get(self, request):
        form = self.crear_form()
        context = {"form": form, 'url': reverse(self.url_string)}
        return TemplateResponse(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            return TemplateResponse(request, self.template_name, {"form": form})
