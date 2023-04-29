from typing import Any
from django.http import HttpRequest
from django.shortcuts import redirect
from datetime import datetime
from django.views.generic import TemplateView,CreateView
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import UserCreationForm
class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today': datetime.today()}

class LoginInterfaceView(LoginView):
    template_name='home/login.html'

class LogoutInterfaceView(LogoutView):
    template_name='home/logout.html'

class SignupInterFaceView(CreateView):
    form_class=  UserCreationForm
    template_name='home/register.html'
    success_url='smart/notes'

    def get(self, request: HttpRequest, *args: str, **kwargs: Any):
        if self.request.user.is_authenticated:
            return redirect('notes.list')
        return super().get(request, *args, **kwargs)