from django.views.generic.edit import FormMixin
from formulario import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    #url corrrespondiente al formulario
    path('', views.FormularioView.as_view(), name = 'formulario'),
]
