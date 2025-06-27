from django.urls import path
from .views import (
    TrafficAccidentListView,
    FilterByCityView,
    FilterByCauseView,
    TrafficAccidentCreateView,
    FilterMultipleView,
    WeekendAccidentView,
)

urlpatterns = [
    path("accidents/", TrafficAccidentListView.as_view(), name="traffic-accident-list"),
    path("accidents/by-city/", FilterByCityView.as_view(), name="filter-by-city"),
    path("accidents/by-cause/", FilterByCauseView.as_view(), name="filter-by-cause"),
    path(
        "accidents/create/", TrafficAccidentCreateView.as_view(), name="accident-create"
    ),
    path(
        "accidents/filter/", FilterMultipleView.as_view(), name="accident-multi-filter"
    ),
    path("accidents/weekend/", WeekendAccidentView.as_view(), name="weekend-accidents"),
]
