from django.urls import path
from . import views # . means current directory

urlpatterns = [
    path('signup/', views.handleSignUp, name='signup'),
]