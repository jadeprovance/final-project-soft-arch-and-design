from django.urls import path
from .views import artwork_list

urlpatterns = [
    path('', artwork_list, name='artwork_list'),
]