from django.shortcuts import render
from app.models import Trips


def home(request):
    return render(request, "app/home.html")


def wildlife(request):
    return render(request, "app/wildlife.html")


def trips(request):
    trips = Trips.objects.all()
    return render(request, "app/trips.html", {'trips': trips})
