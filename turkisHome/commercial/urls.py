from django.urls import path
from . import views

urlpatterns = [
    path('', views.commercial_home, name='commercial_home'),
    path('<int:pk>', views.CommercialDetailView.as_view(), name='commercial-detail')
]