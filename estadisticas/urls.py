from estadisticas.views import EstadisticasView
from django.urls import path
 
urlpatterns = [
    #path('enfermedades', views.EnfermedadListView.as_view(), name = 'enfermedades'),
    #url correspondiente a la seccion de consejos
    path('', EstadisticasView.as_view(), name = 'estadisticas'),
]
