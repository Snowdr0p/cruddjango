from django.urls import path
from .views import index, create, read, update, delete

urlpatterns = [
    path('create/', create, name='create'),
    path('read/', read, name='read'),
    path('update/', update, name='update'),
    path('delete/', delete, name='delete'),
    path('', index),
]