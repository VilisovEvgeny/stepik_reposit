from django.shortcuts import render
from .data import *


def main_view(request):
    context = {
        "title": title,
        "subtitle": subtitle,
        "description": description,
        "departures": departures,
        "tours": tours,

    }
    return render(request, 'tours/index.html', context=context)


def departure_view(request, departure):
    dep = departures[departure]
    context = {
        "title": title,
        "subtitle": subtitle,
        "description": description,
        "departures": departures,
        "tours": tours,
        "departure": departure,
        "dep": dep

    }
    return render(request, 'tours/departure.html', context=context)


def tour_view(request, tour_id):

    context = {
        "title": title,
        "subtitle": subtitle,
        "description": description,
        "departures": departures,
        "departure": departures[tours[tour_id]['departure']],
        "tours": tours[tour_id],
        "tour_id": tour_id,
        "stars": int(tours[tour_id]['stars'])*'★'
    }
    return render(request, 'tours/tour.html', context=context)
