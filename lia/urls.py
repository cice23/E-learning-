from django.urls import path
from .views import generate_lia, lia_list, verify_lia

urlpatterns = [
    path('generate/', generate_lia, name='generate_lia'),
    path('', lia_list, name='lia_list'),
    path('api/v1/verify-lia/', verify_lia, name='verify_lia'),
]
