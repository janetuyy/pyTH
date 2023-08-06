from django.shortcuts import render
from .models import Commercial
from django.views.generic import DetailView


def commercial_home(request):
    commercial = Commercial.objects.all()
    return render(request, 'commercial/com.html', {'commercial': commercial})

class CommercialDetailView(DetailView):
    model = Commercial
    template_name = 'commercial/details_view3.html'
    context_object_name = 'commercial'