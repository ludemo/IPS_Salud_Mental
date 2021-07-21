"""portalWeb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static 
from homepage.views import HomeView

from homepage import views

urlpatterns = [
    #url correspondiente a la seccion admin
    path('admin/', admin.site.urls),
    #url correspondiente a la pagina principal o homepage
    path('', HomeView.as_view(), name = 'home'),
    #incluye a todas las urls de la app formularios
    path('formulario/', include('formulario.urls')),
    #incluye a todas las urls de la app enfermedades
    path('enfermedades/', include('enfermedades.urls'))
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
