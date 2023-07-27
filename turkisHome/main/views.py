from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'main/index.html')

def flats(request):
    return render(request, 'flats/flats.html')

def new(request):
    return render(request, 'main/new.html')

