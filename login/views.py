from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
# Create your views here.


class RegisterUserView(CreateView):
    form_class = RegisterForm
   #succes_url = ''
    template_name = 'register.html'
    model = User

    def get_success_url(self):
        return reverse_lazy('login')
 

class LoginUserView(LoginView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context



