from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    path('index', views.index, name='main'),
    path('flats', views.flats, name='flats'),
    path('new', views.new, name='new'),

]