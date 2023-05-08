from django.urls import path, include # include is added
from . import views # . means current directory

urlpatterns = [
    path('', views.index),
    path('dashboard/', views.dashboard, name='dashboard'),
]