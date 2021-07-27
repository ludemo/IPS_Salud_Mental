from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import RegisterForm
from django.contrib.auth.views import LoginView, LogoutView

# Create your views here.


class RegisterUserView(CreateView):
    form_class = RegisterForm
    succes_url = reverse_lazy('login')
    template_name = 'register.html'

class LoginUserView(LoginView):
    template_name = 'login.html'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context



