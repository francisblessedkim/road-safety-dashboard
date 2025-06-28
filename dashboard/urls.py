from django.urls import path
from .views import (
    TrafficAccidentListView,
    FilterByCityView,
    FilterByCauseView,
    TrafficAccidentCreateView,
    FilterMultipleView,
    WeekendAccidentView,
)

# Define URL patterns for the dashboard app
urlpatterns = [
    # List all traffic accidents
    path("accidents/", TrafficAccidentListView.as_view(), name="traffic-accident-list"),
    
    # Filter accidents by city
    path("accidents/by-city/", FilterByCityView.as_view(), name="filter-by-city"),
    
    # Filter accidents by cause
    path("accidents/by-cause/", FilterByCauseView.as_view(), name="filter-by-cause"),
    
    # Create a new traffic accident record
    path(
        "accidents/create/", TrafficAccidentCreateView.as_view(), name="accident-create"
    ),
    
    # Filter accidents by multiple criteria
    path(
        "accidents/filter/", FilterMultipleView.as_view(), name="accident-multi-filter"
    ),
    
    # List accidents that occurred on weekends
    path("accidents/weekend/", WeekendAccidentView.as_view(), name="weekend-accidents"),
]
