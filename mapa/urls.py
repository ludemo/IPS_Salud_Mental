from mapa.views import MapaView
from django.urls import path
 
urlpatterns = [
    #path('enfermedades', views.EnfermedadListView.as_view(), name = 'enfermedades'),
    #url correspondiente a la seccion de consejos
    path('', MapaView.as_view(), name = 'mapa'),
]
