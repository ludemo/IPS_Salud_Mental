from mapa.views import MapaView
from django.urls import path
 
urlpatterns = [
    #url correspondiente a la seccion de consejos
    path('', MapaView.as_view(), name = 'mapa'),
]
