# user_authentication/views.py

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView


# Login view
class CustomLoginView(LoginView):
    template_name = 'registration/login.html'

# Logout view
class CustomLogoutView(LogoutView):
    template_name = 'registration/logout.html'

# Register view
class CustomRegisterView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/register.html'

