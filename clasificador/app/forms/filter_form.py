from django import forms
from datetime import datetime
from app.models.gasto import Gasto


class FilterForm(forms.Form):

    def __init__(self, *args, user=None, **kwargs):
        super().__init__(*args, **kwargs)

        fecha_actual = datetime.now()

        self.fields['clase'] = forms.ChoiceField(
            choices=self.get_cuentas(),
            label="Cuenta",
            widget=forms.Select(attrs={"class": "form-control"}),
        )
        self.fields['mes'] = forms.ChoiceField(
            choices=self.get_meses(),
            label="Mes",
            initial=fecha_actual.month,
            widget=forms.Select(attrs={"class": "form-control"}),
        )
        self.fields['año'] = forms.ChoiceField(
            choices=self.get_años(),
            label="Año",
            initial=fecha_actual.year,
            widget=forms.Select(attrs={"class": "form-control"}),
        )

    def get_años(self):
        return [(year, str(year)) for year in range(2020, 2030)]

    def get_cuentas(self):
        queryset = Gasto.objects.values("cuenta").filter(
            cuenta__isnull=False).distinct()
        return [(q["cuenta"], q["cuenta"]) for q in queryset]

    def get_meses(self):
        return [
            ("1", "Enero"),
            ("2", "Febrero"),
            ("3", "Marzo"),
            ("4", "Abril"),
            ("5", "Mayo"),
            ("6", "Junio"),
            ("7", "Julio"),
            ("8", "Agosto"),
            ("9", "Septiembre"),
            ("10", "Octubre"),
            ("11", "Noviembre"),
            ("12", "Diciembre"),
        ]
