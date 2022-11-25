from django.urls import path
from . import views


urlpatterns = [

    path('add/', views.newAddRoom, name="newAddRoom"),
    path('rooms/', views.getRooms, name="getRooms"),
    path('room-images/', views.getRoomImages, name="getRoomImages"),
    path('room/', views.roomDeatils, name="roomDeatils"),

]