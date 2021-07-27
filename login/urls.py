from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import LoginViewUser, LogoutView, RegisterView



urlpatterns = [
    path('', LoginViewUser.as_view(), name='login'),
    path('register/', RegisterView, name='register'),
    path('logout/', LogoutView.as_view(), name='logout')


]
