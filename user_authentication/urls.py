# user_authentication/urls.py

from django.urls import path
from .views import CustomLoginView, CustomLogoutView, CustomRegisterView

app_name = 'user_authentication'

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', CustomRegisterView.as_view(), name='register'),
]
