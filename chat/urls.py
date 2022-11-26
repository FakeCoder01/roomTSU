from django.urls import path, include
from . import views


urlpatterns = [
    path('add-message/', views.addMessages, name="addMessages"),
    path('get-messages/', views.getMessages, name="getMessages"),
    path('', views.charView, name="chatView"),
    path('chat-room/', views.createChatRoom, name="createChatRoom"),

]