from django.shortcuts import render
from .models import New
from django.views.generic import DetailView


def new_home(request):
    new = New.objects.all()
    return render(request, 'new/new.html', {'new': new})

class NewDetailView(DetailView):
    model = New
    template_name = 'new/details_view4.html'
    context_object_name = 'new'