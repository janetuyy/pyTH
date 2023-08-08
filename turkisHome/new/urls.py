from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_home, name='new_home'),
    path('<int:pk>', views.NewDetailView.as_view(), name='new-detail')
]