from django.urls import path
from . import views

urlpatterns = [
    path('', views.flats_home, name='flats_home'),
    path('<int:pk>', views.FlatsDetailView.as_view(), name='flats-detail')
]