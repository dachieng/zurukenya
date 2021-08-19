from django.urls import path
from app import views

urlpatterns = [
    path('', views.home, name="home"),
    path('wildlife/', views.wildlife, name="wildlife"),
    path('trips/', views.trips, name="trips"),

]
