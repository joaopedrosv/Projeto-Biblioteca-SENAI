from django.urls import path
from . import views 

#URL inicial
urlpatterns = [
    path('inicio/', views.inicio, name = 'inicio'),
    
]