from django.urls import path
from .views import sandbox_view

urlpatterns = [
    path('', sandbox_view, name='sandbox_view'),
]
