from django.shortcuts import render
from .models import Flats
from django.views.generic import DetailView


def flats_home(request):
    flats = Flats.objects.all()
    return render(request, 'flats/flats.html', {'flats': flats})

class FlatsDetailView(DetailView):
    model = Flats
    template_name = 'flats/details_view1.html'
    context_object_name = 'flats'