from django.urls import path
from .views import distance_view

urlpatterns = [
    path('distance/', distance_view, name='distance'),
]
