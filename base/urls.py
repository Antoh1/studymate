from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='study-home'),
    path('room/', views.room, name='study-room'),
]