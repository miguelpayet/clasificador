from django.urls import path
from . import views

urlpatterns = [
    path("", views.PaginaIndexView.as_view(), name='index'),
    path("ahorro/", views.PaginaAhorrosView.as_view(), name='ahorro'),
    path('clases/', views.ClasesView.as_view(), name='clases'),
    path('gasto/id/<int:id>/', views.GastoView.as_view(), name='gasto'),
    path('resumen-ahorro/', views.ResumenAhorroView.as_view(),
         name='resumen-ahorros'),
    path('search/', views.SearchView.as_view(), name='search'),
]
