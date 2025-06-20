from django.urls import path
from .views import (
    TrafficAccidentListView,
    FilterByCityView,
    FilterByCauseView,
    TrafficAccidentCreateView,
)

urlpatterns = [
    path('accidents/', TrafficAccidentListView.as_view(), name='traffic-accident-list'),
    path('accidents/by-city/', FilterByCityView.as_view(), name='filter-by-city'),
    path('accidents/by-cause/',FilterByCauseView.as_view(), name='filter-by-cause'),
    path('accidents/create/', TrafficAccidentCreateView.as_view(), name='accident-create'),

]