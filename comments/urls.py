# comments/urls.py

from django.urls import path
from .views import comment_list, add_comment

app_name = 'comments'

urlpatterns = [
    path('', comment_list, name='comment_list'),
    path('add/', add_comment, name='add_comment'),
]
