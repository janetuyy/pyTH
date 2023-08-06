from django.shortcuts import render
from .models import Cars
from django.views.generic import DetailView


def cars_home(request):
    cars = Cars.objects.all()
    return render(request, 'cars/cars.html', {'cars': cars})

class CarsDetailView(DetailView):
    model = Cars
    template_name = 'cars/details_view2.html'
    context_object_name = 'cars'