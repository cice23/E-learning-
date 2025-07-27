from django.urls import path
from .views import generate_lia, lia_list

urlpatterns = [
    path('generate/', generate_lia, name='generate_lia'),
    path('', lia_list, name='lia_list'),
]
