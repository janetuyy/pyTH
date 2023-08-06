from django.urls import path
from . import views

urlpatterns = [
    path('', views.cars_home, name='cars_home'),
    path('<int:pk>', views.CarsDetailView.as_view(), name='cars-detail')
]