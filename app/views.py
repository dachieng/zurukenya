from django.contrib.admin.sites import site
from django.http.response import Http404
from django.shortcuts import render
from app.models import Trips, Sites


def home(request):
    return render(request, "app/home.html")


def wildlife(request):
    return render(request, "app/wildlife.html")


def trips(request):
    trips = Trips.objects.all()
    return render(request, "app/trips.html", {'trips': trips})


def search(request):
    if request.method == 'GET':  # this will be GET now
        trip = request.GET.get('search')  # do some research what it does
        try:
            # filter returns a list so you might consider skip except part
            status = Trips.objects.filter(title__icontains=trip)
        except Trips.DoesNotExist:
            raise Http404("Poll does not exist")
        return render(request, "app/search.html", {"trips": status})
    else:
        return render(request, "app/search.html", {})


def sites(request):
    sites = Sites.objects.all()
    return render(request, "app/sites.html", {"sites": sites})
