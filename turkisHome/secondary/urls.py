from django.urls import path
from . import views

urlpatterns = [
    path('', views.secondary_home, name='secondary_home'),
    path('<int:pk>', views.SecondaryDetailView.as_view(), name='secondary-detail')
]