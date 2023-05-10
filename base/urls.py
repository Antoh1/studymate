from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='study-home'),
    path('login/', views.loginPage, name='study-login'),
    path('logout/', views.logoutUser, name='logout-user'),
    path('rigister/', views.registerPage, name='study-register'),
    path('room/<str:pk>/', views.room, name='study-room'),
    path('create-form', views.create_room, name='room-form'),
    path('update-form/<str:pk>/', views.update_room, name='update-form'),
    path('delete-form/<str:pk>/', views.delete_room, name='delete-form'),
    path('delete-comment/<str:pk>/', views.delete_comment, name='delete-comment'),
]