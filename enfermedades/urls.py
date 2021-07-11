from homepage import views
from enfermedades import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 
 
urlpatterns = [
    #url correspondiente a la seccion de consejos
    path('consejos', views.consejos, name = 'consejos'),
    #url correspondiente a la enfermedad depresion
    path('depresion', views.depresion, name = 'depresion'),
    #url correspondiente a la enfermedad alcoholismo
    path('alcoholismo', views.alcoholismo, name = 'alcoholismo'),
    #url correspondiente a la enfermedad psicosis
    path('psicosis', views.psicosis, name = 'psicosis'),
    #url correspondiente a la enfermedad ansiedad
    path('ansiedad', views.ansiedad, name = 'ansiedad'),
    #url correspondiente a violencia familiar
    path('violenciafamiliar', views.violencia_familiar, name = 'violenciafamiliar'),
]
