from django.urls import path
from . import views

urlpatterns = [
    path("", views.IndexView.as_view(), name='index'),
    path('clases/', views.ClasesView.as_view(), name='clases'),
    path('gasto/id/<int:id>/', views.GastoView.as_view(), name='gasto'),
    path('search/', views.SearchView.as_view(), name='search'),
]
