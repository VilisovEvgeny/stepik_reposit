from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_view, name='home'),
    path('departure/<str:departure>', views.departure_view, name='departure'),
    path('tour/<int:tour_id>', views.tour_view, name='tour'),
]