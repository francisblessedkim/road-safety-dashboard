from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.conf import settings
from dashboard.load_data import load_traffic_data
from pathlib import Path
from .models import (
    Location,
    WeatherCondition,
    RoadCondition,
    AccidentCause,
    TrafficAccident,
)
from datetime import date, time

# Test case for the Traffic Accident API endpoints
class TrafficAccidentAPITest(APITestCase):
    def setUp(self):
        # Set up initial data for tests: create related objects in the database
        self.location = Location.objects.create(
            city="Test City", country="Testland", latitude=0.0, longitude=0.0
        )
        self.weather = WeatherCondition.objects.create(description="Clear")
        self.road = RoadCondition.objects.create(description="Dry")
        self.cause = AccidentCause.objects.create(description="Speeding")

        # Create a sample TrafficAccident instance for testing
        self.accident = TrafficAccident.objects.create(
            accident_id="TST123",
            date=date(2025, 6, 20),
            time=time(12, 0),
            location=self.location,
            weather_condition=self.weather,
            road_condition=self.road,
            cause=self.cause,
            vehicles_involved=2,
            casualties=1,
        )

    def test_get_all_accidents(self):
        # Test retrieving all accidents via the API
        response = self.client.get("/api/accidents/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data["results"]), 1)

    def test_filter_by_city(self):
        # Test filtering accidents by city name via the API
        response = self.client.get("/api/accidents/by-city/?city=Test")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data["results"]), 1)

    def test_post_create_accident(self):
        # Test creating a new accident record via the API
        data = {
            "accident_id": "POST123",
            "date": "2025-06-20",
            "time": "15:30:00",
            "location": self.location.id,
            "weather_condition": self.weather.id,
            "road_condition": self.road.id,
            "cause": self.cause.id,
            "vehicles_involved": 3,
            "casualties": 2,
        }
        response = self.client.post("/api/accidents/create/", data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


# Test case for the data seeding script
class DataSeedingTest(APITestCase):
    """
    Tests whether the data seeding script can run without errors.
    """
    def test_load_data_script(self):
        try:
            # Use a relative path to the CSV file for portability
            test_path = Path("data/global_traffic_accidents.csv")
            load_traffic_data(str(test_path))
        except Exception as e:
            # Fail the test if any exception is raised during data loading
            self.fail(f"Seeding script failed with error: {e}")

