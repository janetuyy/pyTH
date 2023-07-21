from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='main'),
    # path('', views.flats, name='flats'),
    # path('new', views.new, name='new')

]