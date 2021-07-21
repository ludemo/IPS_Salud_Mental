from enfermedades.models import Enfermedad
from homepage import views
from enfermedades import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 
 
urlpatterns = [
    #path('enfermedades', views.EnfermedadListView.as_view(), name = 'enfermedades'),
    #url correspondiente a la seccion de consejos
    path('consejos', views.ConsejoView.as_view(), name = 'consejos'),
    #url correspondiente a las enfermedades
    path('<int:pk>', views.EnfermedadDetailView.as_view(), name="enfermedad"),
]
