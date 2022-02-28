from django.shortcuts import render


def main_view(request):
    context = {

    }
    return render(request, 'tours/index.html', context=context)


def departure_view(request):
    context = {

    }
    return render(request, 'tours/departure.html', context=context)


def tour_view(request):
    context = {

    }
    return render(request, 'tours/tour.html', context=context)
