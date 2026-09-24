from django.urls import path
from . import views


urlpatterns = [
    path('', views.inicio, name= 'inicio'),
    path('crear /', views.crear_tareas, name='crear_tareas')
]