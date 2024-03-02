from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Flight, Passenger

# Create your views here.

def index(request):
    return render(request, "flights/index.html", {
        "flights": Flight.objects.all()
})

def flight (request, flight_id):
    flight = Flight.objects.get(pk = flight_id)
    return render(request, "flights/flight.html", {
        "flight": flight,
        "passengers": flight.passengers.all(),
        "non_passenger": Passenger.objects.exclude(flights = flight).all(),
}) 

def book(request, flight_id):
    if request.method == "POST":
        flight = Flight.objects.get(pk = flight_id)
        passenger_id = request.POST['passenger']
        passenger = Passenger.objects.get(pk = passenger_id)
        passenger.flights.add(flight)
        return HttpResponseRedirect(reverse("flights:flight", args = (flight_id,)))
