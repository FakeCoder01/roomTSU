from django.urls import path
from . import views


urlpatterns = [
    path('', views.homePage, name="homePage"),
    path('login/', views.loginPage, name="loginPage"),
    path('new/account/', views.registerPage, name="registerPage"),
    path('new/profile/', views.newProfilePage, name="newProfilePage"),
    path('logout/', views.logoutPage, name="logoutPage"),
]