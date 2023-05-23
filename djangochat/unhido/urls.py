from django.urls import path
from .views import *
from . import views



unhido_patterns = [
      path('', views.general, name='general'),
      path('solicitud/', views.solicitud, name='solicitud'),
      path('crear/', views.crear, name='crear'),
      path('pdf/', views.pdf, name='pdf'),
]
