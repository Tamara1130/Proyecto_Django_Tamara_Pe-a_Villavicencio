from django.urls import path
from .views import random_graphs

urlpatterns = [
    path('', random_graphs, name='random_graphs'),
]
