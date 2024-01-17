from django.urls import path

from . import views

urlpatterns = [
    path('', views.rooms, name='rooms'),
    path('<slug:slug>/', views.room, name='room'),
    path('create_room/', views.create_room, name='create_room'),
    path('room/<slug:slug>/', views.room_with_messages, name='room_with_messages'),
]