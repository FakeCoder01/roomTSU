from django.urls import path
from . import views


urlpatterns = [

    path('add/', views.newAddRoom, name="newAddRoom"),

    path('rooms/', views.getRooms, name="getRooms"),
    path('room-images/', views.getRoomImages, name="getRoomImages"),


    path('room/', views.roomDeatils, name="roomDeatils"),
    path('room/<str:room_id>/', views.RoomPage, name="RoomPage"),

    path('req/', views.roomReqAdd, name="roomReqAdd"),

    # path('review/add/', views.addReview, name="addReview"),
    path('review/<str:room_id>/', views.addReview, name="addReview"),


    path('res/', views.roomResponses, name="roomResponses"),
    path('res/<str:r_id>/', views.ResponseDetail, name="ResponseDetail"),

]