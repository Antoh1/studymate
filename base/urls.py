from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='study-home'),
    path('login/', views.loginPage, name='study-login'),
    path('logout/', views.logoutUser, name='logout-user'),
    path('rigister/', views.registerPage, name='study-register'),
    path('room/<str:pk>/', views.room, name='study-room'),
    path('profile/<str:pk>/', views.userProfile, name='user-profile'),

    path('create-form', views.create_room, name='room-form'),
    path('update-room/<str:pk>/', views.update_room, name='update-room'),
    path('delete-room/<str:pk>/', views.delete_room, name='delete-room'),
    path('delete-comment/<str:pk>/', views.delete_comment, name='delete-comment'),
]