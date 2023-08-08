from django.shortcuts import render
from .models import Secondary
from django.views.generic import DetailView


def secondary_home(request):
    secondary = Secondary.objects.all()
    return render(request, 'secondary/secondary.html', {'secondary': secondary})

class SecondaryDetailView(DetailView):
    model = Secondary
    template_name = 'secondary/details_view5.html'
    context_object_name = 'secondary'