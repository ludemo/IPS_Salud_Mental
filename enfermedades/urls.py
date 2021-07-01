from homepage import views
from enfermedades import views
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 

urlpatterns = [
    path('consejos', views.consejos, name = 'consejos'),
    path('depresion', views.depresion, name = 'depresion'),
]